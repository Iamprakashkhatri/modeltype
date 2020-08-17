from django.urls import path
from . import views
app_name = 'btre'

urlpatterns = [
    path('listing/',views.listing_select_related,name='listing'),
    path('ormquery/',views.ormquery,name='ormquery'),
]