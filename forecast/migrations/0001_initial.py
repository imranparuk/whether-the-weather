# Generated by Django 2.0.6 on 2018-06-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecasts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('min_temp', models.IntegerField()),
                ('max_temp', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('rain_probability', models.IntegerField()),
            ],
        ),
    ]