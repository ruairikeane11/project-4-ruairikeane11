# Generated by Django 4.2.13 on 2024-06-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_books_booking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='number_of_persons',
            field=models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')]),
        ),
    ]