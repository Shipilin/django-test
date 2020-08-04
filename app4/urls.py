from app4 import views
from django.urls import path

# Template tagging
app_name = 'app4'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('', views.index, name='index'),
    # path('registration/', views.registration, name='registration'),
    # path('user_login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('special/', views.special, name='special'),
]
