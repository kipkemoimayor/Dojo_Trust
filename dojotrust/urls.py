from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^dashboard/',views.dashboard,name='dashboard'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^business/(\d+)/',views.single_business,name='single'),
    url(r'^search/',views.search_business,name='search'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
