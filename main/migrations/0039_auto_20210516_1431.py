# Generated by Django 3.2.3 on 2021-05-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_movie_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Documentary', 'Documentary'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller ', 'Thriller'), ('Western', 'Western'), ('War', 'War')], max_length=35),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default='Example: https://i.imgur.com/ID.jpg'),
        ),
    ]
