from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def notify_customer(sender, instance, created, **kwargs):
    if created:
        # Робот только что был добавлен в базу данных
        orders = Order.objects.filter(
            robot_serial=f"{instance.model}-{instance.version}", is_completed=False
        )
        for order in orders:
            customer = order.customer
            send_mail(
                "Робот доступен для заказа",
                f"Добрый день!\nНедавно вы интересовались нашим роботом "
                f"модели {instance.model}, версии {instance.version}.\nЭтот "
                f"робот теперь в наличии. Если вам подходит этот вариант - "
                f"пожалуйста, свяжитесь с нами",
                settings.EMAIL_HOST_USER,
                [customer.email],
                fail_silently=False,
            )


@receiver(post_save, sender=Order)
def update_robot_availability(sender, instance, created, **kwargs):
    with transaction.atomic():
        if created:
            # Заказ только что был создан
            available_robots = Robot.objects.filter(serial=instance.robot_serial, is_available=True)
            if available_robots.exists():
                robot = available_robots.last()
                robot.is_available = False
                robot.save()
                instance.is_completed = True
                instance.save()
