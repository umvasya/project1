from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import UserLoginForm
from .models import Oblast, Gromada, Geoportal
from django.db.models import Count

from otgalbum.serializers import GromadaSerializer


class AllPortals(ListView):
    model = Geoportal
    template_name = 'otgalbum/index.html'
    context_object_name = 'geoportals'
    # queryset = Geoportal.objects.select_related('gromada__geoportal')
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Усі геопортали'
        return context

    def get_queryset(self):
        return Geoportal.objects.filter(type_geoportal='Публічний')

class PortalByOblast(ListView):
    model = Geoportal
    template_name = 'otgalbum/index.html'
    context_object_name = 'geoportals'
    # paginate_by = 6
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Oblast.objects.get(pk=self.kwargs['oblast_id'])
        return context

    def get_queryset(self):
        return Geoportal.objects.select_related().filter(gromada__oblast__id=self.kwargs['oblast_id'], type_geoportal='Публічний')
        # return Geoportal.objects.filter(oblast_id=self.kwargs['oblast_id']).select_related('gromada__oblast_id')

def portal_user_list(request):
    if request.user.is_authenticated:
        geoportals = Geoportal.objects.filter(created_for=request.user)
        return render(request, 'otgalbum/user_portals.html', {'geoportals': geoportals})
    else:
        return render(request, 'otgalbum/index.html')

class PortalByUser(ListView):
    model = Geoportal
    template_name = 'otgalbum/user_portals.html'
    context_object_name = 'geoportals'
    # paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Geoportal.objects.select_related().filter(created_for=2)
        # return Geoportal.objects.filter(oblast_id=self.kwargs['oblast_id']).select_related('gromada__oblast_id')

class SearchResultsView(ListView):
    model = Geoportal
    template_name = 'otgalbum/search_results.html'
    context_object_name = 'geoportals'
    # paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Geoportal.objects.filter(gromada__title__icontains=query)
        return object_list

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['s'] = f"s={self.request.GET.get('s')}&"
    #     return context

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_portals')
    else:
        form = UserLoginForm()
    return render(request, 'otgalbum/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('all_geoportals')

def contact_company(request):
    return render(request, 'otgalbum/contact_company.html')

def geoportal_map(request):
    return render(request, 'otgalbum/geoportal_map.html')

def prices(request):
    return render(request, 'otgalbum/prices.html')

# class GromadaAPIView(generics.ListAPIView):
#     queryset = Gromada.objects.all()
#     serializer_class = GromadaSerializer
#
# class GromadaAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Gromada.objects.all()
#     serializer_class = GromadaSerializer

class GromadaAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class GromadaViewSet(viewsets.ModelViewSet):
    queryset = Gromada.objects.all()
    serializer_class = GromadaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = GromadaAPIListPagination