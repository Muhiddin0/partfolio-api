# Generated by Django 5.0.6 on 2024-05-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0003_alter_moderator_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='location',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='telegram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='tiktok',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]