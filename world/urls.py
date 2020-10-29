from django.urls import path

from . import views

app_name = 'world'

urlpatterns = [
    path('', views.MainMenuView.as_view(), name='main_menu'),
    path('world/<int:pk>/', views.WorldDetailView.as_view(), name='world'),
    path('world/<int:pk>/play/', views.WorldPlayView.as_view(), name='play'),
]
