# Generated by Django 5.0.6 on 2024-06-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="initial_setup_complete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="location",
            field=models.CharField(default="Unknown", max_length=100),
            preserve_default=False,
        ),
    ]
