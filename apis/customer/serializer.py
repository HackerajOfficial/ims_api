from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model = Customer
        fields = ['pk','name','address','mobile','phone']



    def create(self, validated_data):
        customer = Customer(**validated_data)
        customer.save()
        return customer