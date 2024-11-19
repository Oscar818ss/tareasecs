from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/', views.edit_account, name='edit_account'),
    path('delete/', views.delete_account, name='delete_account'),
    path('logout/', views.logout, {'next_page': 'login'}, name='logout'),
]
