# employees/admin.py (complete file)

from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'phone_number', 'birth_date', 'role')
    list_filter = ('role',)
    search_fields = ('name', 'employee_id', 'phone_number')