from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Location, SOSAlert
from .serializers import SOSSerializer

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