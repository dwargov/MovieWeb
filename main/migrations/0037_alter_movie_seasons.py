# Generated by Django 3.2.3 on 2021-05-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_movie_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='seasons',
            field=models.IntegerField(blank=True),
        ),
    ]
