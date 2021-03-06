# Generated by Django 3.1.7 on 2021-03-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20210315_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=50)),
                ('actor_nationality', models.CharField(max_length=20)),
                ('actor_personal_image', models.ImageField(upload_to='actors/pictures')),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_file',
            field=models.FileField(default='null', upload_to='movies/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_category',
            field=models.ManyToManyField(to='hello.Category'),
        ),
    ]
