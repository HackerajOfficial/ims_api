from django.db import models


class Customer(models.Model):
    name = models.TextField(verbose_name="Name")
    address = models.TextField(verbose_name="Address")
    mobile = models.CharField(verbose_name="Mobile", max_length=12)
    phone = models.CharField(verbose_name="Phone", max_length=12)

    class Meta:
        verbose_name_plural = "Customers"
        db_table="customer_db"

    def __str__(self):
        return self.name


