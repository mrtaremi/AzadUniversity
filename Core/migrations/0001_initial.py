# Generated by Django 3.0.9 on 2020-08-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_fa', models.CharField(max_length=255, null=True)),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_fa', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to='news')),
            ],
        ),
    ]
