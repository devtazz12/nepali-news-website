# Generated by Django 4.2.3 on 2023-07-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0009_bichar'),
    ]

    operations = [
        migrations.CreateModel(
            name='bigyanPrabidhi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
    ]
