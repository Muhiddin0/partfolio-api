# Generated by Django 5.0.6 on 2024-05-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reles_date', models.DateField(blank=True, null=True)),
                ('link', models.URLField()),
                ('technology_list', models.ManyToManyField(to='moderator.moderatortechnologylist')),
                ('images', models.ManyToManyField(to='project.projectimages')),
            ],
        ),
    ]
