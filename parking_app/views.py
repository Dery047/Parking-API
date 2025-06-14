from rest_framework import viewsets
from .models import VehicleRecord
from .serializers import VehicleRecordSerializer

class VehicleRecordViewSet(viewsets.ModelViewSet):
    queryset = VehicleRecord.objects.all().order_by('-entry_time')
    serializer_class = VehicleRecordSerializer
