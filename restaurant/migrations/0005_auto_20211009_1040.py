# Generated by Django 3.0.6 on 2021-10-09 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20211007_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='restaurant.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
