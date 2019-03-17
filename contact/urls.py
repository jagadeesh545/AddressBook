"""contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from contact import views

urlpatterns = [
    url(r'^contact_list/$', views.ContactList.as_view(), name='contact_list'),
    url(r'^add_contact/$', views.AddContact.as_view(), name='add_contact'),
    url(r'^view_contact/(?P<pk>[a-zA-z0-9\-]+)$', views.ViewContact.as_view(), name='view_contact'),
    url(r'^delete_contact/(?P<pk>[a-zA-z0-9\-]+)$', views.DeleteContact.as_view(), name='delete_contact'),
]
