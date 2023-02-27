from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.db.models import Avg,Q
from django.http import JsonResponse
from .serializers import *
import base64


# convert img file from database/static folder to base64 string
def imgToBase64(data):
    with data as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data

# get user info of user currently logged in the session
def getUser(id):
    data={}
    if id is not None:
        cust=Customer.objects.get(pk=id)
        data["id"]=cust.pk
        data["FirstName"]=cust.customerFirstName
        data["LastName"]=cust.customerLastName
        data["Username"]=cust.customerUsername
        data["Password"]=cust.customerPassword
        data["Email"]=cust.customerEmail
        data["Address"]=cust.customerAddress
        data["Img"]=imgToBase64(cust.customerImg)
    return data

@api_view(['POST'])
def registerUser(request):
    uname=request.data.get('uname')
    email=request.data.get('email')
    if Customer.objects.filter(Q(customerUsername=uname)).exists():
        return Response({"err":"username already exist"})
    if Customer.objects.filter(customerEmail=email).exists():
        return Response({"err":"email already in use"})
    data={
    'customerFirstName':request.data.get('fname'),
    'customerLastName':request.data.get('lname'),
    'customerUsername':uname,
    'customerPassword':request.data.get('pas'),
    'customerEmail':email,
    'customerAddress':request.data.get('addr'),
    'customerImg':request.data.get('img') 
    }
    result=CustomerSerializer(data=data, partial=True)
    if result.is_valid():
        print("save")
    else:
        del data["customerImg"]
        result=CustomerSerializer(data=data, partial=True)
        if result.is_valid():
            print("save2")
    print(result.errors)
    return JsonResponse({"msg":"user created"})

@api_view(['POST'])
def userLogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user=Customer.objects.get(Q(customerPassword=password)&(Q(customerUsername=username)|Q(customerEmail=username)))
        request.session['user_id'] = user.pk
        return Response(getUser(user.pk))
    except Customer.DoesNotExist:
        return Response({"err":"user not found"})

@api_view(['POST'])
def newPassword(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    user = Customer.objects.filter(customerUsername=username,customerEmail=email)
    if user.exists():
        print(user.values()[0]['customerPassword'])
        return Response({"S":"change"})
    else:
        return Response({"S":"not change"})
def logout(request):
    try:
        id=str(request.session['user_id'])
        del request.session['user_id']
    except:
        return JsonResponse({"msg":"not logged in"})
    return JsonResponse({"msg":"logged out","data":getUser(id)})

@api_view(["GET"])
def allCategories(request,id=0):
    li=[]
    if id==0:
        for i in Category.objects.all():
            dict={
                "id": i.pk,
                "categoryName": i.categoryName,
                "categoryDesc": i.categoryDesc,
                # "categoryImg": imgToBase64(i.categoryImg)
            }
            li.append(dict)
        return Response({"data":li})
    data=Category.objects.get(pk=id)
    dict={
    "id": data.pk,
    "categoryName": data.categoryName,
    "categoryDesc": data.categoryDesc,
    # "categoryImg": imgToBase64(i.categoryImg)
    }
    return Response({"data":dict})


@api_view(["GET"])
def productByCategoty(request,catid):
    li=[]
    for i in ProductCategory.objects.filter(category=catid):
        li.append({
            "id":i.product.pk,
            "name":i.product.productName,
            "price":i.product.productPrice,
            # "img":imgToBase64(i.product.productImg)
        })
    return Response({"data":li})


@api_view(["GET"])
def productDetails(request,pid=0,search=''):
    if pid!=0:
        data=Product.objects.filter(pk=pid)
    elif len(search)!=0:
        data=Product.objects.filter(Q(productName__icontains=search)
                                    |Q(productDesc__icontains=search)
                                    |Q(pk__in=(ProductCategory.objects.filter(category__in=(
                                        Category.objects.filter(categoryName__icontains=search)
                                    ))))).distinct()
    else:
        data=Product.objects.all()
    li=[]
    for i in data:
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
        revli=[]
        for j in Reviews.objects.filter(product=i.pk):
            revli.append({
                "user":j.customer.customerFirstName,
                "img":imgToBase64(j.customer.customerImg),
                "review":j.review
            })
        # dict['reviews']=revli
        li.append(dict)
    return Response({"data":li})
