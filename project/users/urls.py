from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user-register/', views.signup_view, name="user_register"),
    path('user-login/', views.login_view, name="user_login"),
    path('user-logout/', views.logout_view, name="user_logout"),
    path('sell/', views.sell, name='sell'),
    path('luxury-estate/', views.luxury_estate, name='luxury_estate'),
    path('oceanfront-retreats/', views.oceanfront_retreats, name='oceanfront_retreats'),
    path('urban-living/', views.urban_living, name='urban_living'),
    path('countryside_escapes/', views.countryside_escapes, name='countryside_escapes'),
    path('property-search/', views.property_search, name='property_search'),
    path('approve_property/<int:property_id>/', views.approve_property, name='approve_property'),
    path('agent_properties/', views.agent_properties, name='agent_properties'),
    path('owner_properties/', views.owner_properties, name='owner_properties'),
]
