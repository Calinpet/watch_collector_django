from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('watches/', views.watches_index, name='index'),
  path('watches/<int:watch_id>/', views.watches_detail, name='detail'),
]