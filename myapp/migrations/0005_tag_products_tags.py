# Generated by Django 4.2.3 on 2023-08-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='myapp.tag'),
        ),
    ]
