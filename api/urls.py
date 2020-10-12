from django.urls import path

from api.views import VesselViewSet, EquipmentViewSet

urlpatterns = [
    path(
        "vessels",
        VesselViewSet.as_view({"post": "create"}),
        name="vessels-create"
    ),
    path(
        "equipments",
        EquipmentViewSet.as_view({"post": "create"}),
        name="equipments-create",
    ),
]
