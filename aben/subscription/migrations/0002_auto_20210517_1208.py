# Generated by Django 2.2 on 2021-05-17 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stripecustomer',
            old_name='stripeCustomerId',
            new_name='stripe_customer_id',
        ),
        migrations.RenameField(
            model_name='stripecustomer',
            old_name='stripeSubscriptionId',
            new_name='stripe_subscription_id',
        ),
    ]