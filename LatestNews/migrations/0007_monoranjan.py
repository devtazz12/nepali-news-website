# Generated by Django 4.2.3 on 2023-07-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0006_alter_sportsnews_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='monoranjan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
    ]