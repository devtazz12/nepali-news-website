# Generated by Django 4.2.3 on 2023-07-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0005_alter_sportsnews_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsnews',
            name='image_url',
            field=models.URLField(max_length=2000),
        ),
    ]