# Generated by Django 4.2.6 on 2023-12-07 22:32

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0030_alter_entry_passdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
    ]
