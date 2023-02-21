from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('',index),
    path('cat',allCategotyData),
    path('catdata',allCategories),
    path("catprd/<int:catid>",productByCategoty),
    path("prd/<int:pid>",prddetail),
]
