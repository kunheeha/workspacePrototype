# Generated by Django 3.1.7 on 2021-03-18 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0005_auto_20210318_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='todolist',
            new_name='workspace',
        ),
    ]