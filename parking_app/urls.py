from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleRecordViewSet

router = DefaultRouter()
router.register(r'vehicle-records', VehicleRecordViewSet) #Registers the main API endpoint for vehicle records

urlpatterns = [
    path('', include(router.urls)),
]
