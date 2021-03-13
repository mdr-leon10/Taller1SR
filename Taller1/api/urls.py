from django.urls import path
from api import views
from django.conf.urls import url

urlpatterns = [
    # Public endpoints
    path('push/<str:user_id>/', views.push_recommendation_window),
    path('history/<str:user_id>/', views.get_user_history),
    path('login/', views.login),
    path('users/', views.get_all_users),
    path('user/<str:user_query_id>', views.get_user_data),
    path('register/', views.register),
    path('recommendation/<str:user_id>/', views.get_recommendations),
    path('play/', views.play_song),
    path('like/', views.like_artist),
]