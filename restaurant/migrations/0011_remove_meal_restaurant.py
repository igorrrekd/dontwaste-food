# Generated by Django 3.0.6 on 2021-10-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20211014_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='restaurant',
        ),
    ]
