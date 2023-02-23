from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Customer
        fields ='__all__'