from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'phone',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': [
            'phone',
            'telegram',
            'image',
            ]
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': [
            'phone',
            'telegram',
            'image',
            ]
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
