# Generated by Django 2.2 on 2021-05-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("subscription", "0006_auto_20210519_0718")]

    operations = [
        migrations.AlterField(
            model_name="product", name="price", field=models.FloatField()
        )
    ]
