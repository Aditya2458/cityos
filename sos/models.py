from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.latitude},{self.longitude}"


class SOSAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="active")  # active, accepted, resolved
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOS by {self.user} ({self.status})"