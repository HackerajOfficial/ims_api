from django.db import models
from apis.product.models import Product

class Sales(models.Model):
    MODES = (("0","CASH"),("1","CHEQUE"),("2","OTHER"))
    sales_date = models.DateTimeField(auto_now_add=True)
    # bill_no = models.TextField(verbose_name='billnumber', max_length=30)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='quantity')
    selling_price = models.IntegerField(verbose_name='selling_price')
    total = models.FloatField(verbose_name='total')
    payment = models.IntegerField()
    description = models.TextField()
    sub_total = models.FloatField()
    balance = models.FloatField()
    modes = models.CharField(choices=MODES, max_length=2)

    class Meta:
        verbose_name_plural = "SalesDetails"
        db_table = "sales_db"