# Generated by Django 4.2.4 on 2023-08-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_class_classe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classe',
        ),
    ]
