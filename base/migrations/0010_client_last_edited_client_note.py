# Generated by Django 4.1.3 on 2023-11-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_client_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_edited',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
