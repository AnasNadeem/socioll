# Generated by Django 3.2.4 on 2021-07-05 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialsharingapp', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='clubhouse',
            new_name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
