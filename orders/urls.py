from django.urls import path
from .views import ExcelReportView

urlpatterns = [
    path("excel_report/", ExcelReportView.as_view(), name="excel_report"),
]
