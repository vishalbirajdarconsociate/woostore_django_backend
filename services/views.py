from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db.models import Avg
import base64


# convert img file from database/static folder to base64 string
def imgToBase64(data):
    with data as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data


# @api_view(['GET'])
# def index(request):
#     data=Customer.objects.get(customerFirstName='q')
#     return Response({"s":imgToBase64(data.customerImg)})

@api_view(["GET"])
def allCategories(request):
    data=Category.objects.all()
    li=[]
    for i in data:
        dict={
            "id": i.pk,
            "categoryName": i.categoryName,
            "categoryDesc": i.categoryDesc,
            "categoryImg": imgToBase64(i.categoryImg)
        }
        li.append(dict)
    return Response(li)


@api_view(["GET"])
def productByCategoty(request,catid):
    li=[]
    for i in ProductCategory.objects.filter(category=catid):
        li.append({
            "id":i.product.pk,
            "name":i.product.productName,
            "price":i.product.productPrice,
            "img":imgToBase64(i.product.productImg)
        })
    return Response(li)


@api_view(["GET"])
def prddetail(request,pid):
    li=[]
    for i in Product.objects.filter(pk=pid):
        dict={}
        dict['name']=i.productName
        dict['price']=i.productPrice
        dict['thumb']=imgToBase64(i.productImg)
        cat=[]
        for j in ProductCategory.objects.filter(product=i.pk):
            cat.append(j.category.categoryName)
        dict['category']=cat
        dict['description']=i.productDesc
        dict['rating']=Reviews.objects.filter(product=i.pk).aggregate(Avg('rating'))
        dict['rating']=dict['rating']['rating__avg']
        imgli=[]
        for j in ProductImages.objects.filter(product=i.pk):
            imgli.append(imgToBase64(j.image))
        dict['images']=imgli
        li.append(dict)
        revli=[]
        for j in Reviews.objects.filter(product=i.pk):
            revli.append({
                "user":j.customer.customerFirstName,
                "img":imgToBase64(j.customer.customerImg),
                "review":j.review
            })
        dict['reviews']=revli
    return Response(li)


@api_view(["GET"])
def allCategotyData(request):
    catli=[]
    for i in Category.objects.all():
        cat={}
        li=[]
        for j in ProductCategory.objects.filter(category=i.pk):
            prod={}
            data=Product.objects.get(pk=j.product.pk)
            prod['name']=data.productName
            prod['price']=data.productPrice
            prod['thumb']=imgToBase64(data.productImg)
            prodli=[]
            for index,imgs in enumerate(ProductImages.objects.filter(product=j.product.pk)):
                prodli.append(imgToBase64(imgs.image))
            prod['images']=prodli
            li.append(prod)
        cat['category_name']=i.categoryName
        cat['category_img']=imgToBase64(i.categoryImg)
        cat['products']=li
        catli.append(cat)
    return Response({"category":catli})