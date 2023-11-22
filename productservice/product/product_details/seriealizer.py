from .models import products, purchase
from rest_framework import serializers

class product_serializers(serializers.ModelSerializer):
    class Meta:
        model=products
        fields="__all__"
    
class purchase_serializers(serializers.ModelSerializer):
    class Meta:
        model=purchase
        fields="__all__"