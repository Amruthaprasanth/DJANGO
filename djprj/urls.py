"""
URL configuration for djprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from hospital import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hh',views.fun1),
    path('ly',views.fun2),
    path('ht',views.fun3),
    path('y',views.fun4),
    path('h',views.fun5),
    path('z',views.fun6),
    path('fun7',views.fun7),
    path('fun8',views.fun8),
    path('fun9',views.fun9),
    path('fun10',views.fun10),
    path('fun11',views.fun11),
    path('fun12',views.fun12,name='as'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('cus_add',views.cus_add),
    path('cus_display',views.cus_display,name='display_customer'),
    path('cus_update/<int:id>',views.cus_update,name='update_customer'),
    path('cus_delete/<int:id>',views.cus_delete,name='delete_customer'),
    path('ck',views.f15),
    path('cck',views.disb,name='b'),
    path('vl/<int:pk>',views.updatt,name='upd'),
    path('vll/<int:pk>',views.de,name='mk'),
    path('displayCourses',views.course_list),
    path('addStudent',views.add_student),
    path('displayStudents',views.student_list,name='displayStudents'),
    path('displaySpecificStudent/<int:id>',views.displaySpecificStudent,name='dss'),
    path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),
    path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),


]
