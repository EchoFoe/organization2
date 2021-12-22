from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/employees', views.EmployeeList, basename='staff')
# router.register(r'api/departments', views.DepartmentList, basename='staff')

app_name = 'staff'

urlpatterns = format_suffix_patterns([
    path('', views.home, name='home'),
    path('', include(router.urls,)),
    # path('api/employees/', views.EmployeeList.as_view({'get': 'list'}), name='api_employees'),
    # path('api/employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    # path('api/departments/', views.DepartmentList.as_view({'get': 'list'}), name='api_departments'),
])
urlpatterns += router.urls
