from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Buidling

@admin.register(Building)
class BuildingAdmin(LeafletGeoAdmin):
    """
    BuildingAdmin class, inheriting LeafletGeoAdmin
    """

    list_display = (
        'name',
        'building_type',
        'borough',
        'district',
        'pk'
    )

    ordering = ('name',)

    search_fields = (
        'name',
        'building_type',
        'borough',
        'district',
    )
