# Generated by Django 4.2.4 on 2023-08-15 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webersems', '0010_alter_classe_credit_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classe',
            old_name='fa',
            new_name='fall_semester',
        ),
    ]
