"""zeno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from api import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/querystring/$', views.RunQueryViewSet.as_view()),
    url(r'^api/v1/database/$', views.DatabaseViewSet.as_view()),
    url(r'^api/v1/dashboard/$', views.DashboardViewSet.as_view()),
    url(r'^api/v1/dashboard/(?P<dashboard_id>\w+)/query/$', views.QueryViewSet.as_view()),
    url(r'^api/v1/dashboard/(?P<dashboard_id>\w+)/query/(?P<query_id>\w+)$', views.QueryViewSet.as_view()),
]
