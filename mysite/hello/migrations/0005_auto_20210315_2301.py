# Generated by Django 3.1.7 on 2021-03-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20210315_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
