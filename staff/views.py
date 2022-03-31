from django.shortcuts import render
from rest_framework import filters, generics, renderers, viewsets
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Department, Employee, Project
from .serializers import EmployeesSerializer, DepartmentsSerializer, ProjectSerializer, DepartmentDetailSerializer


def home(request):
    return render(request, 'home/home.html')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'


class EmployeeList(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeesSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['last_name', 'department_id']
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    search_fields = ['last_name', 'department__id']
    lookup_field = 'pk'


# class DepartmentList(viewsets.ModelViewSet):
#     queryset = Department.objects.filter(is_active=True)
#     serializer_class = DepartmentsSerializer


class DepartmentList(viewsets.ModelViewSet):
    queryset = Department.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentsSerializer
        if self.action == 'retrieve':
            return DepartmentDetailSerializer
        return DepartmentsSerializer


class ProjectList(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
