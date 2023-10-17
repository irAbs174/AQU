from rest_framework import serializers
from .models import Cart, Support

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'product_id', 'product_title', 'product_title', 'product_collection', 'quantity', 'price', 'image', 'color', 'color_quantity',]
        

class SupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Support
        fields = ['room', 'support_user','message','support_status','timestamp', 'time']