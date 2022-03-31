from rest_framework import serializers
from .models import Department, Employee, Project
from django.urls import reverse


class EmployeesSerializer(serializers.ModelSerializer):
    departments_name = serializers.SerializerMethodField()
    relative_url = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='staff:employee-detail')

    class Meta:
        model = Employee
        fields = ('relative_url', 'url', 'pk', 'last_name', 'first_name', 'middle_name', 'photo', 'function_position',
                  'salary', 'departments_name', 'department')

    def get_departments_name(self, obj):
        return '%s (id=%s)' % (obj.department.name, obj.department.pk)

    def get_relative_url(self, obj):
        return reverse('staff:employee-detail', args=[obj.id])


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('pk', 'name', 'created')


class DepartmentsSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='staff:department-detail')

    class Meta:
        model = Department
        fields = ('pk', 'url', 'name', 'employees_count', 'total_salary')

    def get_employees_count(self, obj):
        return obj.employees.count()

    def get_total_salary(self, obj):
        total_cost = sum(item.salary for item in obj.employees.filter(is_active=True))
        return total_cost


class DepartmentDetailSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Department
        fields = ('pk', 'name', 'projects')
