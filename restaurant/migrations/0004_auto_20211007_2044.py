# Generated by Django 3.0.6 on 2021-10-07 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_category_meal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ('name',)},
        ),
        migrations.AlterIndexTogether(
            name='meal',
            index_together={('id', 'slug')},
        ),
    ]
