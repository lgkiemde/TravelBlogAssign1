# Generated by Django 3.1.6 on 2022-02-15 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0002_auto_20220214_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='favorite_place',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='visited_places',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]