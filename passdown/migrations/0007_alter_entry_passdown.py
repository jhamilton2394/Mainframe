# Generated by Django 4.2.2 on 2023-09-20 04:06

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0006_remove_passdown_date_remove_passdown_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
    ]