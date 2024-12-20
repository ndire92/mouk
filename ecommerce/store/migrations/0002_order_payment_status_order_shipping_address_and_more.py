# Generated by Django 5.1.3 on 2024-11-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='non payé', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='en attente', max_length=100),
        ),
    ]
