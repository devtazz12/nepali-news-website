# Generated by Django 4.2.3 on 2023-07-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0003_horoscopenews_politicalnews_worldnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='topheadlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]
