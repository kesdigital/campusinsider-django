# Generated by Django 4.0.5 on 2022-07-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ontv',
            name='slug',
            field=models.SlugField(blank=True, max_length=180, unique=True),
        ),
    ]
