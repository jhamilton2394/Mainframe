# Generated by Django 4.2.2 on 2023-10-02 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('passdown', '0012_alter_entry_passdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='cdi',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='job_status',
            field=models.CharField(blank=True, choices=[('M1', 'M1'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'), ('M7', 'M7'), ('M8', 'M8'), ('J/C', 'J/C'), ('S/O', 'S/O')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='passdown',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='passdown.passdown'),
        ),
        migrations.AlterField(
            model_name='passdown',
            name='notes',
            field=models.TextField(help_text='This section is for general notes. A/C entries are on the next page.'),
        ),
    ]
