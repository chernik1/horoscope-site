# Generated by Django 4.2.3 on 2023-08-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiac',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]