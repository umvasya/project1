from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from core import settings
# from otgalbum.views import get_all_geoportals,
from otgalbum.views import *


urlpatterns = [
    path('', AllPortals.as_view(), name='all_geoportals'),
    path('oblast/<int:oblast_id>/', PortalByOblast.as_view(), name='oblast'),
    # path('portals/', PortalByUser.as_view(), name='user_portals'),
    path('portals/', portal_user_list, name='user_portals'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact_company/', contact_company, name='contact_company'),
    path('geoportal_map/', geoportal_map, name='geoportal_map'),
    path('prices/', prices, name='prices'),





    # path('api/v1/gromadas_list/', GromadaAPIView.as_view()),
    # path('api/v1/gromada_detail/<int:pk>/', GromadaAPIDetailView.as_view()),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('oblasts/', get_oblast, name='oblasts'),





    # # path('oblast/<int:oblast_id>/', get_oblast, name='oblasts'),
    # # path('oblast/<str:slug>/', PortalByOblast.as_view(), name='by_oblast'),
    # path('search/', Search.as_view(), name='search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)