from django.urls import path
from django.views.generic.base import RedirectView

from tests.views import foo, foo_api

urlpatterns = [
    path("api/foo/", foo_api),
    path("foo/", foo),
    path("bar/", RedirectView.as_view(url="/foo/", permanent=False)),
]
