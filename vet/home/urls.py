from django.urls import path
from home import views


urlpatterns = [
    path('',views.index, name='index'),
    path('AnaSayfa/',views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('animals/', views.animals, name = 'animals'),
    path('add_animal/', views.add_animal, name= 'add_animal'),
    path('animal/<id>/', views.animal_detail, name='animal_detail'),
    path('update_animal/<id>/',views.update_animal, name='update_animal'),
    path('delete/<id>/', views.delete_animal, name='delete_animal'),
]