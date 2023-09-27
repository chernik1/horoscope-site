from django.urls import path
from autification import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout),
    path('register/', views.register),
]