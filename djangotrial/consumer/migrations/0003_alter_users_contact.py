# Generated by Django 5.1.4 on 2025-01-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consumer", "0002_users_contact_users_order_alter_users_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="contact",
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]