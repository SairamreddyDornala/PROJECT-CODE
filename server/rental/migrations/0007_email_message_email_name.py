# Generated by Django 4.1.2 on 2022-11-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_alter_rental_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='message',
            field=models.TextField(default='message'),
        ),
        migrations.AddField(
            model_name='email',
            name='name',
            field=models.CharField(default='name', max_length=254),
        ),
    ]
