# Generated by Django 3.2.3 on 2021-05-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_movie_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.URLField(default=None, null=True),
        ),
    ]
