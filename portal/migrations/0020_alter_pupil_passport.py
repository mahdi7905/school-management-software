# Generated by Django 4.1.2 on 2022-12-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_pupil_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='passport',
            field=models.ImageField(default='profile.jpeg', upload_to='pupil_passports'),
        ),
    ]
