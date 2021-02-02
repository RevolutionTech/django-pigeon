#!/usr/bin/env python
import django
from django.conf import settings
from django.core.management import call_command

if __name__ == "__main__":
    settings.configure(
        DATABASES={
            'default': {
                'NAME': ':memory:',
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=('pigeon',),
        ROOT_URLCONF='tests.urls'
    )
    django.setup()
    call_command('test')
