# Generated by Django 3.2.9 on 2021-12-12 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='last_family',
            new_name='last_name',
        ),
    ]
