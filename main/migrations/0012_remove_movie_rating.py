# Generated by Django 3.0.14 on 2021-05-14 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
    ]
