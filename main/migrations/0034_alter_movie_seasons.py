# Generated by Django 3.2.3 on 2021-05-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_movie_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='seasons',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
