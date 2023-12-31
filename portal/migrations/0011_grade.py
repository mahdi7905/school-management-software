# Generated by Django 4.1.2 on 2022-12-27 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_teacher_arm_teacher_grade_teacher_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conventional_grade', models.CharField(blank=True, choices=[('nursery1', 'nursery 1'), ('nursery2', 'nursery 2'), ('grade1', 'grade 1'), ('grade2', 'grade 2'), ('grade3', 'grade 3'), ('grade4', 'grade 4'), ('grade5', 'grade 5'), ('grade6', 'grade 6')], max_length=10, null=True)),
                ('conventional_arm', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E')], max_length=10, null=True)),
                ('islamiya_grade', models.CharField(blank=True, choices=[('nursery1', 'nursery 1'), ('nursery2', 'nursery 2'), ('grade1', 'grade 1'), ('grade2', 'grade 2'), ('grade3', 'grade 3'), ('grade4', 'grade 4'), ('grade5', 'grade 5'), ('grade6', 'grade 6')], max_length=10, null=True)),
                ('islamiya_arm', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E')], max_length=10, null=True)),
                ('pupil', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.pupil')),
                ('teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.teacher')),
            ],
        ),
    ]
