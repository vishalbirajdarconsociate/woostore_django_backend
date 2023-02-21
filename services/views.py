from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http import FileResponse
import base64


# convert img file from database/static folder to base64 string
def imgToBase64(data):
    with data as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data


@api_view(['GET'])
def index(request):
    data=Customer.objects.get(customerFirstName='q')
    return Response({"s":imgToBase64(data.customerImg)})

@api_view(["GET"])
def categotyData(request):
    cat={}
    catli=[]
    for i in Category.objects.all():
        li=[]
        prod={}
        for j in ProductCategory.objects.filter(category=i.pk):
            data=Product.objects.get(pk=j.product.pk)
            prod['name']=data.productName
            prod['price']=data.productPrice
            prod['img']=imgToBase64(data.productImg)
            li.append(prod)
        cat['category_name']=i.categoryName
        cat['category_img']=imgToBase64(i.categoryImg)
        cat['products']=li
        catli.append(cat)
    return Response({"category":catli})