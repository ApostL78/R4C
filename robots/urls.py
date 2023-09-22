from django.urls import path
from .views import CreateRobotView

urlpatterns = [
    path('create_robot/', CreateRobotView.as_view(), name='create_robot'),
]