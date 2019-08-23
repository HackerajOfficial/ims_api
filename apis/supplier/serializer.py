from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.supplier.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model = Supplier
        fields = ['pk','name','address','mobile','phone']



    def create(self, validated_data):
        supplier = Supplier(**validated_data)
        supplier.save()
        return supplier