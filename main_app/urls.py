from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('events/', views.event_index, name='event-index'),
  path('events/<int:event_id>/', views.event_detail, name='event-detail'),
  path('events/create/', views.EventCreate.as_view(), name='event-create'),
  path('events/<int:pk>/update', views.EventUpdate.as_view(), name='event-update'),
  path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event-delete'),
]