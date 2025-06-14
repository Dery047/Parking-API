from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleRecordViewSet

router = DefaultRouter()
router.register(r'vehicle-records', VehicleRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
