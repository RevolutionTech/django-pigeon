from django.conf.urls import url

from pigeon.tests.views import foo


urlpatterns = [
    url(r'^foo/$', foo),
]
