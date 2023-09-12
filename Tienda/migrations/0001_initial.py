# Generated by Django 4.2.2 on 2023-09-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.CharField(blank=True, max_length=254)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
