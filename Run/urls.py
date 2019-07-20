"""Pict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
app_name='Run'
urlpatterns = [
    path('sorting/',views.Sorter.as_view(),name='sorting'),
    path('',views.Login.as_view(),name='login'),
    #path('Excel/',views.Excel,name='Excel'),
    path('register/',views.Register.as_view(),name='register'),
    path('postlogin/',views.Postlog.as_view(),name='postlogin'),
    path('logoff/',views.logoff,name='logoff'),
    path('student/',views.Student.as_view(),name='student'),
    path('faculty/',views.Faculty.as_view(),name='faculty'),
    path('report/',views.Report.as_view(),name='reports'),
    path('conf/',views.Conf.as_view(),name='conf'),
    path('conf/<int:id>',views.conf_delete),
    path('web/',views.Web.as_view(),name='web'),
    path('web/<int:id>',views.web_delete),
    path('collab/',views.Collaboration.as_view(),name='collab'),
    path('collab/<int:id>',views.collab_delete),
    path('coi/',views.Ind.as_view(),name='coi'),
    path('coi/<int:id>',views.coi_delete),
    path('isl/',views.Laboratory.as_view(),name='isl'),
    path('isl/<int:id>',views.isl_delete),
    path('rgs/',views.RG.as_view(),name='rgs'),
    path('rgs/<int:id>',views.rgs_delete),
    path('rgd/',views.RG1.as_view(),name='rgd'),
    path('rgd/<int:id>',views.rgd_delete),
]
