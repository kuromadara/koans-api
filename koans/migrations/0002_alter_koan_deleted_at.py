# Generated by Django 4.1.3 on 2022-11-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("koans", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="koan",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
