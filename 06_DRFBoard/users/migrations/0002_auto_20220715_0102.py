# Generated by Django 3.1.14 on 2022-07-14 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="subject",
            new_name="subjects",
        ),
    ]
