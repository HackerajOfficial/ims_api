from django.db import models


class Category(models.Model):
    
    product_name           =   models.TextField(verbose_name="product_name")
    category_name          =   models.TextField(verbose_name="category_name", unique=True)
    
    
    class Meta:
        verbose_name_plural =   "Categories"
        db_table            =   "category_db"

    def __str__(self):
        return self.product_name