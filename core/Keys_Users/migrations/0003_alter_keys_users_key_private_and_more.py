# Generated by Django 4.2.5 on 2023-11-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Keys_Users", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keys_users",
            name="key_private",
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name="keys_users",
            name="key_public",
            field=models.CharField(max_length=900),
        ),
    ]