# Generated by Django 4.2.13 on 2024-05-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]