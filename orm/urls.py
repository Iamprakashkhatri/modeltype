from django.urls import path
from . import views
app_name = 'orm'

urlpatterns = [
    path('book_list',views.book_list,name='book_list'),
]