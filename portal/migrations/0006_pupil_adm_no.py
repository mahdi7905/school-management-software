# Generated by Django 4.1.2 on 2022-12-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_rename_first_name_pupil_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='ADM_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]