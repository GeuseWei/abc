# Generated by Django 4.1.6 on 2023-02-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_student_delete_userinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
            ],
        ),
        migrations.DeleteModel(
            name="Student",
        ),
    ]
