# Generated by Django 2.2 on 2021-05-18 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_auto_20210518_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='subscription.Customer'),
        ),
    ]
