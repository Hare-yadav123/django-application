# Generated by Django 5.0.2 on 2024-06-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copper", "0003_login_signupmodel_conform_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactModel",
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
                ("your_name", models.CharField(max_length=100)),
                ("working_mail", models.EmailField(max_length=100)),
                ("company_website", models.CharField(max_length=100)),
                ("feed_back", models.TextField(max_length=100)),
            ],
        ),
    ]
