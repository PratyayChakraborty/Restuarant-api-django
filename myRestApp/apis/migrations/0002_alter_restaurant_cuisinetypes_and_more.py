# Generated by Django 4.1.6 on 2023-03-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cuisineTypes',
            field=models.CharField(choices=[('South Indian', 'South Indian'), ('Korean', 'Korean'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('French', 'French'), ('north indian', 'north indian'), ('East indian', 'East indian')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='isOpen',
            field=models.BooleanField(choices=[(True, True), (False, False)], default=True),
        ),
    ]
