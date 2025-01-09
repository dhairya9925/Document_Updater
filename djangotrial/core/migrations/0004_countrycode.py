# Generated by Django 5.1.4 on 2025-01-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_delete_countrycode"),
    ]

    operations = [
        migrations.CreateModel(
            name="countryCode",
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
                ("country", models.CharField(max_length=100)),
                ("dialCode", models.CharField(max_length=5)),
                ("image", models.CharField(max_length=100)),
            ],
        ),
    ]