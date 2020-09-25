from django.urls import path
from . import views

app_name='mangoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_user, name='logout')
]
