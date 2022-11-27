# lernpfad/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account, QuizAnswer
from .forms import UserCreationForm, UserChangeForm


class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'phone', 'date_of_birth', 'is_staff',  'is_superuser', 'get_quiz_answers')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password', 'get_quiz_answers')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()
    
    readonly_fields = ('get_quiz_answers',)


admin.site.register(Account, AccountAdmin)
admin.site.register(QuizAnswer)