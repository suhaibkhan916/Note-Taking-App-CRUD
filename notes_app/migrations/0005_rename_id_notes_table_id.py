# Generated by Django 4.2.1 on 2023-05-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0004_alter_notes_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='id',
            new_name='table_id',
        ),
    ]
