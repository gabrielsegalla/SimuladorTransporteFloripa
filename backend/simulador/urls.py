from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView
from app import views


class DocsView(APIView):
    def get(self, request, *args, **kwargs):
        apidocs = {
            'district': request.build_absolute_uri('district/'),
            'region': request.build_absolute_uri('region/'),
            'ticket': request.build_absolute_uri('ticket/'),
            'journey': request.build_absolute_uri('journey/'),
        }
        return Response(apidocs)


router = routers.DefaultRouter()
router.register(r'district', views.DistrictViewSet)
router.register(r'region', views.RegionViewSet)
router.register(r'ticket', views.TicketBusViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('journey/', views.JourneyView.as_view(), name='journey')
]