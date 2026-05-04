from django.urls import path
from .views import send_sos

urlpatterns = [
    path('sos/', send_sos),
]