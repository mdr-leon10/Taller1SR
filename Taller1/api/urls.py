from django.urls import path
from api import views
from django.conf.urls import url

urlpatterns = [
    # Public endpoints
    path('login/', views.login),
    path('register/', views.register),
    path('recommendation/<user>/', views.give_recommendations),
    path('listen/<song>/', views.increase_number_counts),
 ]
    
    # Login
