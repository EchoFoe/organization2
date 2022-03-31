from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/employees', views.EmployeeList, basename='employee')
router.register(r'api/departments', views.DepartmentList, basename='department')
router.register(r'api/projects', views.ProjectList, basename='project')

app_name = 'staff'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls,)),
    path('api/employees/', views.EmployeeList.as_view({'get': 'list'}), name='api_employees'),
    path('api/departments/', views.DepartmentList.as_view({'get': 'list'}), name='api_departments'),
    path('api/projects/', views.ProjectList.as_view({'get': 'list'}), name='api_projects')
]
urlpatterns += router.urls
