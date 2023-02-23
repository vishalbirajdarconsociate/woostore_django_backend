from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('',index),
    path('login/',userLogin),
    path('logout/',logout),
    path('allCategories/',allCategories),
    path('allCategories/<int:id>',allCategories),
    path("catprd/<int:catid>",productByCategoty),
    path("prd/",prddetail),
    path("prd/<int:pid>",prddetail),
]
