# Generated by Django 3.2.18 on 2023-05-16 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_addproduct_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
