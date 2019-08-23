from django.db import models


class Supplier(models.Model):
    name = models.TextField(verbose_name="Name")
    address = models.TextField(verbose_name="Address")
    mobile = models.CharField(verbose_name="Mobile", max_length=12)
    phone = models.CharField(verbose_name="Phone", max_length=12)

    class Meta:
        verbose_name_plural = "Suppliers"
        db_table="supplier_db"

    def __str__(self):
        return self.name


