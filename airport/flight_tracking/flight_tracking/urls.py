"""flight_tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

API_TITLE = "Flight Tracking"

router = routers.DefaultRouter()
router.register(r'airports', views.AirportViewSet,'airports')
router.register(r'flights', views.FlightViewSet,'flights')
router.register(r'count',views.CountViewSet,'count')

schema_view = get_swagger_view(title=API_TITLE)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path("docs/",schema_view),
]