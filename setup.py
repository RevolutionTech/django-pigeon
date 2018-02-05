#!/usr/bin/env python
from setuptools import setup, find_packages, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import django
        from django.conf import settings
        from django.core.management import call_command

        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3',
                }
            },
            INSTALLED_APPS=('pigeon',),
            ROOT_URLCONF='pigeon.tests.urls'
        )
        django.setup()
        call_command('test', 'pigeon')


setup(
    name='django-pigeon',
    version='0.3.0',
    packages=find_packages(),
    license='ISC License',
    description='Test utilities for Django projects.',
    url='https://github.com/RevolutionTech/django-pigeon/',
    author='Lucas Connors',
    author_email='lucas@revolutiontech.ca',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    install_requires=[
        'six',
        'Django >= 1.8',
    ],
    cmdclass={'test': TestCommand},
)
