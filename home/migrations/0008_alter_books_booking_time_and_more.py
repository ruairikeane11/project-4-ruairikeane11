# Generated by Django 4.2.13 on 2024-06-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_books_number_of_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='booking_time',
            field=models.CharField(choices=[('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30')], max_length=5),
        ),
        migrations.AlterField(
            model_name='books',
            name='number_of_persons',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], max_length=2),
        ),
    ]
