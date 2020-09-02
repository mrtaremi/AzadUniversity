# Generated by Django 3.0.9 on 2020-08-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='text',
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_fa',
            field=models.TextField(null=True),
        ),
    ]