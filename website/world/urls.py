from django.urls import path

from . import views

app_name = 'world'

urlpatterns = [
    path('', views.MainMenuView.as_view(), name='main_menu'),
    path('realities/', views.RealityListView.as_view(), name='reality_index'),
    path('reality/<int:pk>/', views.RealityDetailView.as_view(), name='reality'),
    path('reality/<int:pk>/play/', views.RealityPlayView.as_view(), name='play'),
    path('update_profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]
