
from django.urls import path

from . import views


urlpatterns = [
    path('',views.user_profile, name='user_profile'),
    path('update/', views.user_update, name="user_update"),
    path('password/', views.change_password, name="change_password"),
]