from django.urls import path
from .views import send_sos, get_alerts, accept_alert

urlpatterns = [
    path('sos/', send_sos),
     path('alerts/', get_alerts),
    path('accept-alert/', accept_alert),
]