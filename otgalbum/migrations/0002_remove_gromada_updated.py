# Generated by Django 4.0.4 on 2022-05-06 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otgalbum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gromada',
            name='updated',
        ),
    ]
