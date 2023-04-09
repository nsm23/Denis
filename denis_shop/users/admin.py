from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'phone')
    ordering = ('-username',)
    list_display = ('username', 'email', 'phone',
                    'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "birth_year",
                    "password",
                    "avatar",
                    "is_superuser",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
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
