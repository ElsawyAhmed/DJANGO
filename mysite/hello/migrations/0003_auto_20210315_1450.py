# Generated by Django 3.1.7 on 2021-03-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_tasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
