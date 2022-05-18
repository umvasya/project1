from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from otgalbum.models import Oblast, Gromada, Geoportal

# Register your models here.
class OblastAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class GromadaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'oblast', 'title', 'slug', 'tg_type', 'area', 'created')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('oblast',)
    # list_editable = ('area',)
    fields = ('oblast', 'title', 'slug', 'tg_type', 'area',)
    readonly_fields = ('created',)
    save_on_top = True
    list_per_page = 20

class GeoportalAdmin(admin.ModelAdmin):
    list_display = ('id', 'gromada', 'type_geoportal', 'show_portal_url', 'get_photo', 'created', 'views', 'is_active')
    list_display_links = ('id', )
    search_fields = ('gromada',)
    list_editable = ('is_active', 'type_geoportal', 'views',)
    list_filter = ('type_geoportal', 'gromada',)
    fields = ('gromada', 'type_geoportal', 'portal_url', 'created_for', 'image', 'get_photo', 'views', 'is_active')
    readonly_fields = ('get_photo', 'created')
    save_on_top = True
    list_per_page = 20

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_photo.short_description = 'Фото'

    def show_portal_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>Link</a>", url=obj.portal_url)

    show_portal_url.short_description = "Посилання на геопортал"


# Register your models here.
admin.site.register(Oblast, OblastAdmin)
admin.site.register(Gromada, GromadaAdmin)
admin.site.register(Geoportal, GeoportalAdmin)


admin.site.site_title = "Адміністрування порталів"
admin.site.site_header = "Адміністрування сайту"