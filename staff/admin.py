from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['name', 'is_active', 'created']
    list_display = ['name', 'is_active', 'created']
    search_fields = ['name', 'employees__last_name']
    list_editable = ['is_active']
    date_hierarchy = 'created'
    list_filter = ['employees__function_position', 'is_active', 'created']
    readonly_fields = ['created']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('last_name', 'first_name', 'middle_name'), 'function_position', 'photo', 'salary', 'department',
              'is_active', 'created']
    list_display = ['photo_img', 'full_name', 'function_position', 'salary', 'department', 'is_active', 'created']
    list_display_links = ['full_name']
    search_fields = ['last_name']
    list_editable = ['salary', 'department', 'is_active']
    date_hierarchy = 'created'
    list_filter = ['department', 'is_active', 'created']
    readonly_fields = ['created']
