from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu-list/', views.menu_list, name='menu-list'),
    path('menu-detail/', views.menu_detail, name='menu-detail'),
    path('add-menu-item/', views.add_menu_item, name='menu-add'),
    path('chef-list/', views.chef_list, name='chef-list'),
    path('add-chef/', views.add_chef, name='chef-add'),
    path('category-list/', views.category_list, name='category-list'),
]
