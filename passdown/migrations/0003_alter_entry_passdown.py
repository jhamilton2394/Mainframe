# Generated by Django 4.2.2 on 2023-09-20 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0002_alter_entry_passdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
    ]
