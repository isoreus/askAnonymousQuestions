# Generated by Django 4.2 on 2023-08-09 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="user",),
    ]
