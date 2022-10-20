from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='index'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.homeUsers,name='home'),
    path('logout/',views.logoutUser,name='logout'),
]
