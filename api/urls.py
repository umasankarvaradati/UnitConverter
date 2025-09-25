from django.urls import path
from mainApp.views import UnitConverterAPI

urlpatterns = [
    path('convert/',UnitConverterAPI.as_view(),name="api-converter")
]