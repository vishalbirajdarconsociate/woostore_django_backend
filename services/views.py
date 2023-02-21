from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http import FileResponse
import base64


# Create your views here.
@api_view(['GET'])
def index(request):
    data=Customer.objects.get(customerFirstName='q')
    print()
    with data.customerImg as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return Response({"s":image_data})