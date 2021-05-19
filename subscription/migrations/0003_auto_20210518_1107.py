# Generated by Django 2.2 on 2021-05-18 11:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0002_auto_20210517_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='StripeCustomer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='stripe_customer_id',
            new_name='stripe_id',
        ),
    ]