from django.conf.urls import url

from pigeon.tests.views import foo, foo_api


urlpatterns = [
    url(r'^api/foo/$', foo_api),
    url(r'^foo/$', foo),
]
