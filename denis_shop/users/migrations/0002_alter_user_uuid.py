# Generated by Django 4.2 on 2023-04-10 18:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                auto_created=True,
                default=uuid.uuid4,
                editable=False,
                unique=True,
                verbose_name="uuid",
            ),
        ),
    ]
