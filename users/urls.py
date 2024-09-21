from django.urls import path, include
from .views import register_user, login
urlpatterns = [
    path('logar/', login, name='login'),
    path('register/', register_user, name='register_user')
]
