# Generated by Django 5.0.7 on 2024-07-31 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_role_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]