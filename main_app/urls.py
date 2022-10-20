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
  path('straps/', views.StrapList.as_view(), name='straps_index'),
  path('straps/<int:pk>/', views.StrapDetail.as_view(), name='straps_detail'),
  path('straps/create/', views.StrapCreate.as_view(), name='straps_create'),
  path('straps/<int:pk>/update/', views.StrapUpdate.as_view(), name='straps_update'),
  path('straps/<int:pk>/delete/', views.StrapDelete.as_view(), name='straps_delete'),
  path('watches/<int:watch_id>/assoc_strap/<int:strap_id>/', views.assoc_strap, name='assoc_strap'),
  path('accounts/signup/', views.signup, name='signup'),
]