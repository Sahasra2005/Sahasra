# Generated by Django 4.2.3 on 2023-08-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dateCreated',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]