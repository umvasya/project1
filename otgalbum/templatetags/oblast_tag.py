from django import template
from django.db.models import Count

from otgalbum.models import Oblast

register = template.Library()

@register.simple_tag(name='get_list_oblasts')
def get_oblasts():
    return Oblast.objects.filter(gromada__geoportal__type_geoportal='Публічний').order_by('id').distinct().annotate(cnt=Count('gromada'))
    # return Oblast.objects.select_related().annotate(cnt=Count('gromada')).filter(cnt__gt=0).filter(gromada__geoportal__type_geoportal='Публічний').order_by('id')
    # return Oblast.objects.annotate(cnt=Count('gromada')).filter(cnt__gt=0, ).order_by('id')

@register.inclusion_tag('otgalbum/oblast.html')
def show_oblast():
    # categories = Category.objects.all()
    oblaststag = Oblast.objects.annotate(cnt=Count('gromada')).filter(cnt__gt=0).order_by('name')
    # oblasts = Oblast.objects.annotate(cnt=Count('gromada')).filter(cnt__gt=0).order_by('id')
    return {'oblaststag': oblaststag}