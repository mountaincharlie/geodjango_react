from django.contrib.gis.db import models  # db from djangorestframework_gis

from django.utils.translation import gettext_lazy as _  # helping with translation (need this?)


BOROUGH_CHOICES = [
    ('Westminster', 'Westminster'),
    ('City of London', 'City of London'),
    ('Islington', 'Islington'),
    ('Hackney', 'Hackney'),
    ('Lambeth', 'Lambeth'),
]

BUILDING_TYPE = [
    ('Coffee shop', 'Coffee shop'),
    ('Offices', 'Offices'),
    ('Restaurant', 'Restaurant'),
    ('Supermarket', 'Supermarket'),
    ('Hotel', 'Hotel'),
    ('Petrol station', 'Petrol station'),    
]

# building model
class Building(models.Model):
    name =  models.Charfield(_('Building Name'), max_length=100)
    borough = models.Charfield(_('Building Borough'), max_legnth=30, choices=BOROUGH_CHOICES)
    district = models.Charfield(_('Building District'), max_legnth=50)
    building_type = models.Charfield(_('Building Type'), max_length=30, choices=BUILDING_TYPE)
    reviews = models.IntegerField(_('Number of reviews'), default=0)
    open_24hours = models.BooleanField(_('Open 24 Hours'), default=False)
    address = models.Charfield(_('Building Address'), max_length=60)
    location = models.PointField(_('Building Location'), srid=4326)  # 4326 => lat/lon
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Date Updated'), auto_now=False)

    def __str__(self):
        return self.name
    
    # def get_building_type(self):
    #     return self.building_type

