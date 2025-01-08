
from django.urls import path, re_path
from {{ cookiecutter.project_slug }}.views import HealthChecker

urlpatterns = [
    re_path(r"^$", view=HealthChecker.as_view(), name="HealthChecker"),
]

