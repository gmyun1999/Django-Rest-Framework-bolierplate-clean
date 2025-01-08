{% raw %}
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from "{{ cookiecutter.project_slug }}".settings import ENV


class HealthChecker(APIView):
    print(cookiecutter.project_slug)
    def get(self, request):
        return JsonResponse(
            data={"status": "success", "ENV": ENV},
            status=status.HTTP_200_OK,
        )
{% endraw %}
