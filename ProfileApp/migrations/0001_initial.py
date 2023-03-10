# Generated by Django 4.1.5 on 2023-02-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForm',
            fields=[
                ('id', models.CharField(default='', max_length=6, primary_key=True, serialize=False)),
                ('series', models.CharField(default='', max_length=100)),
                ('bodyTypes', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('system', models.CharField(default='', max_length=100)),
                ('price', models.FloatField(default='', max_length=100)),
                ('net', models.IntegerField(default=0.0)),
            ],
        ),
    ]
