# Generated by Django 5.0.6 on 2024-08-12 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0002_alter_notification_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notifications',
        ),
    ]
