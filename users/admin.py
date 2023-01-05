# lernpfad/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account, QuizAnswer, Notizen, Onboarding
from .forms import UserCreationForm, UserChangeForm


class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'nachname', 'vorname', 'phone', 'date_of_birth', 'is_staff',  'is_superuser', 'get_quiz_answers')
    list_filter = ('is_superuser',)

    fieldsets = (
        ('Info', {'fields': ('nachname', 'vorname', 'date_of_birth', 'get_quiz_answers', 'picture')}),
        (None, {'fields': ('email', 'password')}),
        ('Groups', {'fields': ('groups',)}),
        
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('nachname', 'vorname', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'nachname', 'phone')
    ordering = ('email',)
    filter_horizontal = ()
    
    readonly_fields = ('get_quiz_answers',)

admin.site.register(Onboarding)
admin.site.register(Account, AccountAdmin)
admin.site.register(QuizAnswer)
admin.site.register(Notizen)
