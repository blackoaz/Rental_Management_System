# Generated by Django 4.1 on 2022-09-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental_houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apartment_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='descption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]