# Generated by Django 5.0.4 on 2024-07-23 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_number',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_number',
            new_name='last_name',
        ),
    ]
