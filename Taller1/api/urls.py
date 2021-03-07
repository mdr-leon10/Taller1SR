from django.urls import path
from api import views
from django.conf.urls import url

urlpatterns = [
    # Public endpoints
    path('login/', views.login),
    path('user/<str:user_query_id>', views.get_user_data),
    path('register/', views.register),
    path('recommendation/<str:user_id>/', views.get_recommendations),
    path('listen/<str:song_id>/', views.increase_number_counts),
]