from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('createtrip',views.createtrip,name="createtrip"),
    path('profile',views.profile,name="profile"),
    path('tripinfo',views.tripinfo,name="tripinfo"),
    path('viewtrips',views.viewtrips,name="viewtrips")
]
