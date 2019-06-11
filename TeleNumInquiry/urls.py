"""TeleNumInquiry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from testmodle import views
urlpatterns = [
    path('', views.mylogin, name="mylogin"),
    path('admin/', admin.site.urls),
    path('cdh/', views.cdh),
    path('xdh/', views.xdh,name = "xdh"),
    path('comments_upload/', views.comments_upload, name="comments_upload"),
    path('mylogin/', views.mylogin, name="mylogin"),
    path('tianxie/', views.tianxie),
    path('tianxie/<param>/', views.tianxie, name="tianxie"),
    path('mylogout', views.mylogout,name ="mylogout"),
    # path('chaxunextend/', views.chaxunextend),

]
