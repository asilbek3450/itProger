# Generated by Django 5.0.1 on 2024-01-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon raqam'),
        ),
    ]