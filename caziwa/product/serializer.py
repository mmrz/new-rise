from rest_framework import serializers
from django.db.models import Q
from .models import Product,ProductPrice,ProductOption,ProductQuantity,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','image']



class ProductSerializer(serializers.ModelSerializer):
    pro_cat = CategorySerializer(source='category')

    class Meta:
        model = Product
        fields = ['pro_cat','name','description_short','description']