from django.urls import path
from .import views

urlpatterns = [
    path('', views.patient_signup, name='patient_signup'),

    path('/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    # Add URLs for patient and doctor dashboards
]
