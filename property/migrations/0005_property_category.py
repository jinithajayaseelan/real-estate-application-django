# Generated by Django 3.0.3 on 2020-05-11 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Category'),
        ),
    ]