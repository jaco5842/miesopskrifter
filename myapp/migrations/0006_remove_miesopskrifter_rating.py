# Generated by Django 4.1.7 on 2023-05-14 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_miesopskrifter_oprindelse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miesopskrifter',
            name='rating',
        ),
    ]
