from django.db import models


class Product(models.Model):
    CATEGORY = (("0","Electronics"),("1","Accessories"))
    product_name  = models.TextField(verbose_name="product_name")
    category_name = models.CharField(choices=CATEGORY, max_length=2)
    # no_of_product = models.IntegerField()
    
    
    class Meta:
        verbose_name_plural =   "Product"
        db_table            =   "product_db"

    def __str__(self):
        return self.product_name