# Generated by Django 4.2.4 on 2023-08-15 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webersems', '0018_alter_classe_options_remove_semester_classes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='class2',
        ),
    ]
