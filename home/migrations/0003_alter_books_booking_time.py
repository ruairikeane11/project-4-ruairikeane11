# Generated by Django 4.2.13 on 2024-06-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_books_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='booking_time',
            field=models.TimeField(choices=[('14:00', '14:30'), ('15:00', '15:00'), ('16:00', '16:30'), ('17:00', '17:30'), ('18:00', '18:30'), ('19:00', '19:30'), ('20:00', '20:30'), ('21:00', '21:30'), ('22:00', '22:30')]),
        ),
    ]
