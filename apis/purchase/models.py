from django.db import models
from django.urls import reverse
from apis.supplier.models import Supplier

class StockDetails(models.Model):
    product_name        =   models.TextField(verbose_name="product_name")
    category            =   models.TextField(verbose_name="category_name")
    buying_rate         =   models.IntegerField()
    selling_rate        =   models.IntegerField()
    supplier_name       =   models.ForeignKey(Supplier,  on_delete=models.SET_NULL, null=True)
    expire_date         =   models.DateField()

    class Meta:
        verbose_name_plural =   "StockDetails"
        db_table            =   "stock_db"

    # def get_absolute_url(self):
    #     return reverse("add_stock_details", kwargs={"category": self.get_category_display().lower(), "pk":self.pk})


class Purchase(models.Model):
    MODES = (("0","CASH"),("1","CHEQUE"),("2","OTHER"))
    purchase_date = models.DateTimeField(auto_now_add=True)
    bill_no = models.TextField(verbose_name='billnumber', max_length=30)
    product_name = models.TextField(verbose_name='product_name', max_length=20)
    quantity = models.IntegerField(verbose_name='quantity')
    cost_price = models.IntegerField(verbose_name='cost_price')
    selling_price = models.IntegerField(verbose_name='selling_price')
    stock = models.IntegerField(verbose_name='stock')
    total = models.FloatField(verbose_name='total')
    payment = models.IntegerField()
    description = models.TextField()
    sub_total = models.FloatField()
    balance = models.FloatField()
    modes = models.CharField(choices=MODES, max_length=2)
    due_date = models.DateField()

    class Meta:
        verbose_name_plural = "PurchaseDetails"
        db_table = "purchase_db"
