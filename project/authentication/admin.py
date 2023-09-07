from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from project.authentication.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_per_page = 20
    fieldsets = [
        [
            None,
            {
                "fields": [
                    "email",
                    "password",
                ],
            },
        ],
        [
            _("Permissions"),
            {
                "fields": [
                    "email_verified",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_deleted",
                    "groups",
                    "user_permissions",
                ],
            },
        ],
        [
            _("Important dates"),
            {
                "fields": [
                    "last_login",
                ],
            },
        ],
    ]
    add_fieldsets = [
        [
            None,
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "email",
                    "password1",
                    "password2",
                ],
            },
        ],
    ]
    list_display = [
        "email",
        "date_joined",
        "is_staff",
        "is_deleted",
    ]
    list_filter = [
        "email_verified",
        "is_staff",
        "is_superuser",
        "is_active",
        "is_deleted",
        "groups",
    ]
    search_fields = [
        "email",
    ]
    ordering = ["-date_joined", "email"]
    filter_horizontal = [
        "groups",
        "user_permissions",
    ]
