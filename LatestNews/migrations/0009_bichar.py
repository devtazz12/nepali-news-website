# Generated by Django 4.2.3 on 2023-07-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LatestNews', '0008_rename_horoscopenews_upatiyaka'),
    ]

    operations = [
        migrations.CreateModel(
            name='bichar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
    ]
