# Generated by Django 4.0.2 on 2022-04-19 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cajaMenorApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
    ]
