# Generated by Django 4.1.2 on 2022-12-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='long',
            field=models.TextField(default='Empty', max_length=1024),
            preserve_default=False,
        ),
    ]