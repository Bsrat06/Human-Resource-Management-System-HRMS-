from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Department
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'firstname', 'last_name', 'is_staff', "get_groups"]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'groups'),
        }),
    )
    ordering = ('email',)  # Use 'email' for ordering instead of 'username'
    
    def get_groups(self, obj):
        return ", ".join(group.name for group in obj.groups.all())
    get_groups.short_description = 'Groups'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Employee)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

