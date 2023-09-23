from datetime import datetime, timedelta
from io import BytesIO

import pandas as pd
import pytest
from django.test import RequestFactory
from django.urls import reverse

from robots.models import Robot
from .views import ExcelReportView


@pytest.fixture
def robots():
    return [
        ("M1", "V1"),
        ("M1", "V2"),
        ("M2", "V1"),
        ("M2", "V2"),
        ("M2", "V2"),
    ]


@pytest.fixture
def create_robots(robots):
    for robot in robots:
        Robot.objects.create(
            model=robot[0],
            version=robot[1],
            created=datetime.now() - timedelta(days=1),
        )


@pytest.mark.django_db
def test_excel_report_view(create_robots):
    factory = RequestFactory()
    request = factory.get(reverse("excel_report"))
    response = ExcelReportView.as_view()(request)

    assert response.status_code == 200
    assert (
        response["Content-Type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    assert response["Content-Disposition"] == (
        "attachment; " "filename=robot_report.xlsx"
    )

    df = pd.read_excel(BytesIO(response.content), sheet_name=None)

    assert set(df.keys()) == {"M1", "M2"}

    model1_sheet = df["M1"]
    assert len(model1_sheet) == 2
    assert set(model1_sheet.columns) == {"Модель", "Версия", "Количество за неделю"}
    assert set(model1_sheet["Версия"]) == {"V1", "V2"}
    assert set(model1_sheet["Количество за неделю"]) == {1, 1}

    model2_sheet = df["M2"]
    assert len(model2_sheet) == 2
    assert set(model2_sheet.columns) == {"Модель", "Версия", "Количество за неделю"}
    assert set(model2_sheet["Версия"]) == {"V1", "V2"}
    assert set(model2_sheet["Количество за неделю"]) == {1, 2}
