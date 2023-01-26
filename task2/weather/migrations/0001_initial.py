# Generated by Django 4.1.5 on 2023-01-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.IntegerField()),
                ('atmosphere_pressure', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]