# Generated by Django 4.1.5 on 2024-10-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movie_data_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_data',
            name='homepage',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie_data',
            name='original_title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie_data',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
