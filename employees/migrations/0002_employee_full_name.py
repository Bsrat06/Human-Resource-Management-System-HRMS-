# Generated by Django 5.0.7 on 2024-07-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
