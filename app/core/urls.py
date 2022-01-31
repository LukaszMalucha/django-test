from django.urls import path
from core.views import home, failed_response

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("failed_response", failed_response, name="failed_response")

]