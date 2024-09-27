from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('repair/', views.repair, name='repair'),
    path('replace/', views.replace, name='replace'),
    path('aircond_log/', views.aircond_log, name='aircond_log'),
    path('complain/', views.complain, name='complain'),
    path('refill_log/', views.refill_log, name='refill_log'),
    path('adhoc_item/', views.adhoc_item, name='adhoc_item'),
    path('add_aircond/', views.addAircond, name='add_aircond'),
    path('add_repair/', views.addRepair, name='add_repair'),
    path('add_item/', views.addItem, name='add_item'),
    #path('menu_list/', views.MenuList.as_view(), name='MenuList'),
    #path('menu_item_detail/', views.MenuItemDetail.as_view(), name='MenuItemDetail'),
    #path('testing/', views.Testing.as_view(), name='Testing'),
]
