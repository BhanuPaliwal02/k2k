from django.contrib import admin
from django.urls import path
from k2k import views


urlpatterns =[
    path("lookupdata/", views.lookupdata, name= "lookupdata" ),
    path("r_district_data/", views.district_data, name= "r_district_data" ),
    path("r_farmingassets/", views.farmingassets, name= "r_farmingassets" ),
    path("lookupdata/", views.lookupdata, name= "lookupdata" ),
    path("user_data/", views.user_data, name= "user_data" ),
    path("state_district/", views.state_district, name= "state_district" ),
    path('admin/', admin.site.urls)
]