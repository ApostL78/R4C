import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Robot
from .utils import validate_robot_data


@method_decorator(csrf_exempt, name='dispatch')
class CreateRobotView(View):
    def post(self, request):
        data = json.loads(request.body)
        model = data.get("model")
        version = data.get("version")
        created = data.get("created")
        serial = f"{model}-{version}"
        data["serial"] = serial

        # Валидация входных данных
        error = validate_robot_data(data)
        if error:
            return JsonResponse(status=400, data={"error": error})

        # Создание новой записи в базе данных
        robot = Robot(model=model, version=version, serial=serial,
                      created=created)
        robot.save()

        return JsonResponse({"success": "Robot created successfully"})
