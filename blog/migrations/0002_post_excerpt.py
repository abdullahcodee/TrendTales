# Generated by Django 5.0.6 on 2024-07-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="excerpt",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
