# Generated by Django 4.1.6 on 2023-02-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0005_user_birthday_user_email_user_gender_user_major_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(default="2000-01-01"),
        ),
    ]
