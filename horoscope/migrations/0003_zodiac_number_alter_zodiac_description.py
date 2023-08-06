# Generated by Django 4.2.3 on 2023-08-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0002_alter_zodiac_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='zodiac',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
