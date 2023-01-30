from django.contrib import admin
from .models import CustomUser
# Register your models here.

# from users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import *
# admin.site.register(CustomUser)
admin.site.register(Profile)
# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# admin.site.register(Profile)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

# class CustomUserAdmin(admin.ModelAdmin):
#     exclude = ('password')
#     ordering = ('email',)
#     list_display = ('email', 'first_name', 'last_name', 'is_superuser')
#     search_fields = ('email', 'first_name', 'last_name')
#     list_filter = ('is_superuser',)
#     readonly_fields = ('email',)
    
# admin.site.register(CustomUser, CustomUserAdmin)
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ("email", "is_staff", "is_active",)
#     list_filter = ("email", "is_staff", "is_active",)
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "email", "password1", "password2", "is_staff",
#                 "is_active", "groups", "user_permissions"
#             )}
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)


# admin.site.register(CustomUser, CustomUserAdmin)
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)