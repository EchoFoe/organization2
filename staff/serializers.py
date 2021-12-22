from rest_framework import serializers
from .models import Department, Employee
from django.urls import reverse


class EmployeesSerializer(serializers.ModelSerializer):
    departments_name = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()
    # url = serializers.HyperlinkedIdentityField(view_name='staff:employee-detail')

    class Meta:
        model = Employee
        fields = ('absolute_url', 'pk', 'last_name', 'first_name', 'middle_name', 'photo', 'function_position',
                  'salary', 'departments_name', 'department')

    def get_departments_name(self, obj):
        return '%s (id=%s)' % (obj.department.name, obj.department.pk)

    def get_absolute_url(self, obj):
        return reverse('staff:employee_detail', args=[obj.id])


class DepartmentsSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('pk', 'name', 'employees_count', 'total_salary')

    def get_employees_count(self, obj):
        return obj.employees.count()

    def get_total_salary(self, obj):
        total_cost = sum(item.salary for item in obj.employees.all())
        return total_cost
