# Generated by Django 3.1.7 on 2021-03-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_todoitem_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='importance',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
