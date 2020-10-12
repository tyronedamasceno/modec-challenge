from django.urls import path

from api.views import VesselViewSet, EquipmentViewSet, equipments_inactivate

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
    path(
        "vessels/<vessel>/active-equips",
        EquipmentViewSet.as_view({"get": "list"}),
        name="equipments-by-vessel"
    ),
    path(
        "equipments/inactivate",
        equipments_inactivate,
        name="equipments-inactivate"
    )
]
