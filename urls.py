"""
URL configuration for hostel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from hostel.views import  allocate_room, home, room_details,student_home, student_list, student_login, student_register, visitor_request, visitor_request_status, visitor_request_success ,create_announcement,create_announcement

urlpatterns = [
    path('admin/', admin.site.urls),
   path('home/', home, name='home'),
    path('student_register/', student_register, name='student_register'),
    path('student_login/', student_login, name='student_login'),
    # path('admin_login/', admin_login, name='admin_login'),
   
    path('student_home/',student_home, name='student_home'),
    path('admin/allocate-room/', allocate_room, name='allocate_room'),
    # path('admin/home/', admin_home, name='admin_home'),
    
    path('admin/student-list/',student_list, name='student_list'),
    path('admin/room-details/', room_details, name='room_details'),
 path('visitor/request/', visitor_request, name='visitor_request'),
 path('visitor/request/success/', visitor_request_success, name='visitor_request_success'),
 path('create_announcement/', create_announcement, name='create_announcement'),
    # path('edit-student/<int:pk>/', edit_student, name='edit-student'),
# path('visitor-request-status/<str:usn>/', visitor_request_status, name='visitor_request_status'),
]