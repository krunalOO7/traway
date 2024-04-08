from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('find',views.find,name="find"),
    path('view',views.view,name="view"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path('practice',views.practice,name="practice"),

]