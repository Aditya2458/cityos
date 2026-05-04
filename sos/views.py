from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Location, SOSAlert
from .serializers import SOSSerializer
from .serializers import SOSAlertSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_sos(request):
    serializer = SOSSerializer(data=request.data)

    if serializer.is_valid():
        lat = serializer.validated_data['latitude']
        lon = serializer.validated_data['longitude']

        # Save location
        location = Location.objects.create(
            user=request.user,
            latitude=lat,
            longitude=lon
        )

        # Create SOS alert
        sos = SOSAlert.objects.create(
            user=request.user,
            location=location
        )

        return Response({
            "message": "SOS sent",
            "sos_id": sos.id
        })

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_alerts(request):
    user = request.user

    # Only volunteers can see alerts
    if not user.is_volunteer:
        return Response({"error": "Not authorized"}, status=403)

    alerts = SOSAlert.objects.filter(status="active").order_by('-created_at')
    serializer = SOSAlertSerializer(alerts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_alert(request):
    user = request.user

    if not user.is_volunteer:
        return Response({"error": "Not authorized"}, status=403)

    alert_id = request.data.get("alert_id")

    try:
        alert = SOSAlert.objects.get(id=alert_id, status="active")
        alert.status = "accepted"
        alert.save()

        return Response({"message": "Alert accepted"})
    except SOSAlert.DoesNotExist:
        return Response({"error": "Alert not found or already taken"}, status=404)