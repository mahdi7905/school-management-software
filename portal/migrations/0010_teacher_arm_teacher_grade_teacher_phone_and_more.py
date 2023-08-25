# Generated by Django 4.1.2 on 2022-12-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_remove_pupil_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Arm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Grade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
