# Generated by Django 4.2.4 on 2023-08-15 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webersems', '0008_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='class_num',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='credit_hours',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='fa',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='school',
        ),
        migrations.AddField(
            model_name='semester',
            name='classes',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
