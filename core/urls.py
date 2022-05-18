from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from otgalbum.views import *

router = routers.DefaultRouter()
router.register(r'gromada', GromadaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('otgalbum.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls')),
]
