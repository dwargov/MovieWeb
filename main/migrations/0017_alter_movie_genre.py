# Generated by Django 3.2.3 on 2021-05-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Fantasy', 'Fantasy'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('Sci-Fi', 'Sci-Fi'), ('Thriller ', 'Thriller'), ('Western', 'Western'), ('War', 'War'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Animation', 'Animation')], max_length=35),
        ),
    ]
