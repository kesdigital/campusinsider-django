# Generated by Django 4.0.5 on 2022-07-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_alter_ontv_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ontv',
            name='on_tv_type',
            field=models.CharField(choices=[('MOVIE', 'Movie'), ('SERIE', 'Serie')], default='MOVIE', max_length=5),
        ),
    ]
