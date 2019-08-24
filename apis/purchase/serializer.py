from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.purchase.models import StockDetails, Purchase


class StockSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')

        if context:
            self.request = context.get('request')


    class Meta:
        model = StockDetails
        fields = ['pk','product_name','category','buying_rate','selling_rate','supplier_name','expire_date']

    def create(self, validated_data):
        stock = StockDetails(**validated_data)
        stock.save()
        return stock



class PurchaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('context')


    class Meta:
        model = Purchase
        fields = ['pk','purchase_date','bill_no','product_name','quantity','cost_price','selling_price','total','payment','description','sub_total','balance','modes']
        read_only_fields = ['stock']

    def create(self, validated_data):
        purchase = Purchase(**validated_data)
        purchase.save()
        return purchase