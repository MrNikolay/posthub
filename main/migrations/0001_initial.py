# Generated by Django 4.1.2 on 2022-12-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=32)),
                ('short', models.TextField(max_length=165)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=24, unique=True)),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=12, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('is_banned', models.BooleanField(default=False)),
            ],
        ),
    ]
