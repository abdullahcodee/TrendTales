# Generated by Django 5.0.6 on 2024-07-09 11:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_excerpt"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="img_name",
            new_name="image",
        ),
    ]
