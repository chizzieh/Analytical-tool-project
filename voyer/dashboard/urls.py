from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-index'),
    path('dashboard', views.dashboard, name='dashboard-index'),
    # Other URL patterns if any
]
