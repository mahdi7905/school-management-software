# Generated by Django 4.1.2 on 2022-12-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_application_other_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.TextField(max_length=1000)),
                ('Content', models.TextField(max_length=10000)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='contentImages')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
