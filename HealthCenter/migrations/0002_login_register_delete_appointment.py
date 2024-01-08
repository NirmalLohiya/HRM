# Generated by Django 4.2.7 on 2023-12-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HealthCenter", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
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
                ("lemail", models.CharField(max_length=30)),
                ("lpassword", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Register",
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
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name="Appointment",
        ),
    ]
