# Generated by Django 4.2.4 on 2023-08-15 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webersems', '0011_rename_fa_classe_fall_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='credit_hours',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=4, max_length=1),
        ),
    ]
