# Generated by Django 2.0.2 on 2018-02-04 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
