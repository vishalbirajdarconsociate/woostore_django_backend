from django.contrib import admin
from django.urls import path,include
from services.views import *
urlpatterns = [
    path('login/',userLogin),
    path('logout/',logout),
    path('new/',registerUser),
    path('change/',newPassword),
    path('allCategories/',allCategories),
    path('allCategories/<int:id>',allCategories),
    path("catprd/<int:catid>",productByCategoty),
    path("product/",productDetails),
    path("product/<int:pid>",productDetails),
    path("product/search/<str:search>",productDetails),
]
