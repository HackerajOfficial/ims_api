# Generated by Django 2.2.2 on 2019-08-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('bill_no', models.TextField(max_length=30, verbose_name='billnumber')),
                ('product_name', models.TextField(max_length=20, verbose_name='product_name')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('cost_price', models.IntegerField(verbose_name='cost_price')),
                ('selling_price', models.IntegerField(verbose_name='selling_price')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('total', models.FloatField(verbose_name='total')),
                ('payment', models.IntegerField()),
                ('description', models.TextField()),
                ('sub_total', models.FloatField()),
                ('balance', models.FloatField()),
                ('modes', models.CharField(choices=[('0', 'CASH'), ('1', 'CHEQUE'), ('2', 'OTHER')], max_length=2)),
                ('due_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'PurchaseDetails',
                'db_table': 'purchase_db',
            },
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(verbose_name='product_name')),
                ('category', models.TextField(verbose_name='category_name')),
                ('buying_rate', models.IntegerField()),
                ('selling_rate', models.IntegerField()),
                ('expire_date', models.DateField()),
                ('supplier_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.Supplier')),
            ],
            options={
                'verbose_name_plural': 'StockDetails',
                'db_table': 'stock_db',
            },
        ),
    ]
