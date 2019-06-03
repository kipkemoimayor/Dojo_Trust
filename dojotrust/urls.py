from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='home')
]
