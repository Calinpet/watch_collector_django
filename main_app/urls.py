from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('watches/', views.watches_index, name='index'),
  path('watches/<int:watch_id>/', views.watches_detail, name='detail'),
  # new route used to show a form and create a cat
  path('watches/create/', views.WatchCreate.as_view(), name='watches_create'),
  # Add the new routes below
  path('watches/<int:pk>/update/', views.WatchUpdate.as_view(), name='watches_update'),
  path('watches/<int:pk>/delete/', views.WatchDelete.as_view(), name='watches_delete'),
  path('watches/<int:watch_id>/add_service/', views.add_service, name='add_service'),
]