# Generated by Django 4.1.2 on 2022-11-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0004_remove_rental_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
