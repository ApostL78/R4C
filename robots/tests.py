import json

import pytest
from django.urls import reverse

from robots.models import Robot


def get_valid_robot_data():
    return {"model": "AB", "version": "01", "created": "2022-09-23T12:00:00Z"}


@pytest.mark.django_db
def test_create_robot_success(client):
    data = get_valid_robot_data()
    response = client.post(
        reverse("create_robot"), data=json.dumps(data), content_type="application/json"
    )
    assert response.status_code == 200
    assert json.loads(response.content) == {"success": "Robot created successfully"}
    robot = Robot.objects.get(serial="AB-01")
    assert robot.is_available is True


def test_create_robot_failure(client):
    data = get_valid_robot_data()
    data["model"] = "ABC"
    response = client.post(
        reverse("create_robot"), data=json.dumps(data), content_type="application/json"
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_robot_serial(client):
    data = get_valid_robot_data()
    response = client.post(
        reverse("create_robot"), data=json.dumps(data), content_type="application/json"
    )
    assert response.status_code == 200
    assert Robot.objects.filter(serial="AB-01").exists()
