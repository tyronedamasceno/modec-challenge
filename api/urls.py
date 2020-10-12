from django.urls import path

from api.views import VesselViewSet

urlpatterns = [
    path('vessels', VesselViewSet.as_view({'post': 'create'}),
         name='vessels-create'),
]
