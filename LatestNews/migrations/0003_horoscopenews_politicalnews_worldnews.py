# Generated by Django 4.2.3 on 2023-07-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0002_sportsnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoroscopeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='politicalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='worldNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
    ]