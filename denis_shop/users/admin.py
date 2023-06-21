from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile


class UserAdminConfig(UserAdmin):
    search_fields = ("email", "username", "phone", "is_verified")
    ordering = ("-username",)
    list_display = (
        "username",
        "email",
        "phone",
        "is_staff",
        "is_superuser",
        "is_active",
        "is_verified",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "birthday",
                    "password",
                    "avatar",
                    "is_superuser",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_verified")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile)
