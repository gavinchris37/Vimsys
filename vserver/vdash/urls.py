from django.urls import path

from . import views

urlpatterns = [
    path('vdash/', views.dashboard, name='dashboard'),
    #path('vdash/', views.projects, name='projects'),
    path('vdash/<str:pk>/', views.dashboardviews, name='dashboardviews'),
]
