from datetime import timedelta
from io import BytesIO

import pandas as pd
from django.utils import timezone
from pandas import DataFrame

from robots.models import Robot


def _get_robot_data_last_week():
    start_date = timezone.now() - timedelta(days=7)
    robots = Robot.objects.filter(
        created__gte=start_date, created__lte=timezone.now()
    ).values_list("model", "version")
    return list(robots)


def _create_excel_file(robots):
    df = DataFrame(robots, columns=["Модель", "Версия"])
    grouped = (
        df.groupby(["Модель", "Версия"])
        .size()
        .reset_index(name="Количество за неделю")
    )

    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    for model in grouped["Модель"].unique():
        model_data = grouped[grouped["Модель"] == model]
        model_data.to_excel(writer, sheet_name=model, index=False)

    writer.close()
    output.seek(0)
    return output
