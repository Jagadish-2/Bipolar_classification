from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reg',views.reg,name='reg'),
    path('home',views.home,name='home'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('login2',views.login2,name="login2"),
    path('rcomplete',views.rcomplete,name="rcomplete"),
    path('bipolar',views.bipolar,name="bipolar"),
    path('predBipolar',views.predBipolar,name='predBipolar'),
    path('bipolarSv',views.bipolarSv,name='bipolarSv')
]