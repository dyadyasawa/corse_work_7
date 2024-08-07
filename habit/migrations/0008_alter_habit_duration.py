# Generated by Django 4.2.2 on 2024-06-29 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0007_rename_user_habit_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="duration",
            field=models.DurationField(
                default=datetime.timedelta(seconds=120),
                verbose_name="Продолжительность выполнения",
            ),
        ),
    ]
