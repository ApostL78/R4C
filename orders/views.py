from django.http import HttpResponse
from django.views import View

from orders.utils import _get_robot_data_last_week, _create_excel_file


class ExcelReportView(View):
    def get(self, request, *args, **kwargs):
        robots = _get_robot_data_last_week()
        output = _create_excel_file(robots)

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument"
            ".spreadsheetml.sheet"
        )
        response["Content-Disposition"] = "attachment; filename=robot_report.xlsx"
        response.write(output.getvalue())
        return response
