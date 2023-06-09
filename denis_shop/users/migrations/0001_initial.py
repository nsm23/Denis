# Generated by Django 4.2 on 2023-04-09 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=64,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, upload_to="", verbose_name="profile_foto"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="birthday"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "phone",
                    phone_field.models.PhoneField(
                        blank=True, max_length=12, verbose_name="phone"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="admin"),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date_created"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "unique_together": {("username", "email", "phone")},
            },
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=128, verbose_name="first name")),
                ("surname", models.CharField(max_length=256, verbose_name="lastname")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
