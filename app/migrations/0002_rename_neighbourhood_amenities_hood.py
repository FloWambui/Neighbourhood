# Generated by Django 4.0.4 on 2022-06-22 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenities',
            old_name='neighbourhood',
            new_name='hood',
        ),
    ]
