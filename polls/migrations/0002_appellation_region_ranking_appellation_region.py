# Generated by Django 4.2.2 on 2023-09-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('initials', models.CharField(blank=True, db_index=True, max_length=10, null=True)),
                ('appellation', models.ManyToManyField(to='polls.appellation')),
            ],
        ),
        migrations.AddField(
            model_name='appellation',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.region'),
        ),
    ]
