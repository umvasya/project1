# Generated by Django 4.0.4 on 2022-05-06 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otgalbum', '0005_remove_gromada_created_for_remove_gromada_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoportal',
            name='gromada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geoportal', to='otgalbum.gromada', verbose_name='Громада'),
        ),
    ]
