from django.conf.urls import url
from django.views.generic.base import RedirectView

from tests.views import foo, foo_api

urlpatterns = [
    url(r"^api/foo/$", foo_api),
    url(r"^foo/$", foo),
    url(r"^bar/$", RedirectView.as_view(url="/foo/", permanent=False)),
]
