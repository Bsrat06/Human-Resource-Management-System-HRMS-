# Generated by Django 5.0.6 on 2024-08-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.EmailField(default='123@gmail.com', max_length=254),
        ),
    ]