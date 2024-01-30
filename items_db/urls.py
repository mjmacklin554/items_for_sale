from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list_item', views.list_item, name="list-item"),
    path('add_item', views.add_item, name="add-item"),
    path('show_list/<list_id>', views.show_list, name="show-list"),
    path('search_item', views.search_item, name="search-item"),
   
]
