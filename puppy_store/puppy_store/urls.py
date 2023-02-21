from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('puppies.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls)
]
