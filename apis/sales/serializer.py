from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.sales.models import Sales

class SalesSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model = Sales
        fields = ['pk','product_name']



    def create(self, validated_data):
        sales = Sales(**validated_data)
        sales.save()
        return sales