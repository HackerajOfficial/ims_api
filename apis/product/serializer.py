from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model = Product
        fields = ['pk','product_name','category_name']