"""
URL configuration for life_care project.

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
from health.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('',Index,name='home'),
    path('admin_login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('view_doctor/',view_Doctor,name='view_doctor'),
    path('add_doctor/',add_Doctor,name='add_doctor'),
    path('delete_doctor(?P<int:pid>)',delete_Doctor,name='delete_doctor'),
    path('view_patient/',view_Patient,name='view_patient'),
    path('add_patient/',add_Patient,name='add_patient'),
    path('delete_patient(?P<int:pid>)',delete_Patient,name='delete_patient'),
    path('view_appointment/',view_Appointment,name='view_appointment'),
    path('add_appointment/',add_Appointment,name='add_appointment'),
    path('delete_appointment(?P<int:pid>)',delete_Appointment,name='delete_appointment'),
]
