# Generated by Django 4.1.2 on 2022-12-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_alter_teacher_arm_alter_teacher_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='Conventional_Grade',
            field=models.CharField(choices=[('nursery1', 'nursery 1'), ('nursery2', 'nursery 2'), ('grade 1', '1'), ('grade 2', '2'), ('grade 3', '3'), ('grade 4', '4'), ('grade 5', '5'), ('grade 6', '6')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='Islamiya_Grade',
            field=models.CharField(choices=[('nursery1', 'nursery 1'), ('nursery2', 'nursery 2'), ('grade 1', '1'), ('grade 2', '2'), ('grade 3', '3'), ('grade 4', '4'), ('grade 5', '5'), ('grade 6', '6')], max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Grade',
            field=models.CharField(blank=True, choices=[('nursery1', 'nursery 1'), ('nursery2', 'nursery 2'), ('grade 1', '1'), ('grade 2', '2'), ('grade 3', '3'), ('grade 4', '4'), ('grade 5', '5'), ('grade 6', '6')], max_length=50, null=True),
        ),
    ]