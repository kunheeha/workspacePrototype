# Generated by Django 3.1.7 on 2021-03-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_folder_pathname'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
