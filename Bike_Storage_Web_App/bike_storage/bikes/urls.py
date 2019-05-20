from django.urls import path

from . import views

urlpatterns = [
	path('', views.bike_list, name='bike_list'),
    path('new', views.bike_create, name='bike_new'),
    path('edit/<int:pk>', views.bike_update, name='bike_edit'),
    path('delete/<int:pk>', views.bike_delete, name='bike_delete'),
    path('detail/<int:pk>', views.bike_view, name='bike_detail'),
]