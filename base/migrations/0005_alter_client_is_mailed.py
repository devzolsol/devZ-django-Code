# Generated by Django 4.1.3 on 2023-10-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_client_address_alter_client_address_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="is_mailed",
            field=models.BooleanField(default=False),
        ),
    ]
