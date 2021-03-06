# Generated by Django 2.2 on 2021-05-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("subscription", "0012_auto_20210523_0828")]

    operations = [
        migrations.RemoveField(model_name="subscription", name="plan"),
        migrations.AddField(
            model_name="subscription",
            name="currency",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="subscription",
            name="description",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="subscription",
            name="name",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="subscription", name="price", field=models.FloatField(default=0)
        ),
        migrations.AddField(
            model_name="subscription",
            name="product_id",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.DeleteModel(name="Product"),
    ]
