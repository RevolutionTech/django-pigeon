# django-pigeon
#### Test utilities for Django projects

[![Build Status](https://travis-ci.org/RevolutionTech/django-pigeon.svg?branch=master)](https://travis-ci.org/RevolutionTech/django-pigeon)
[![codecov](https://codecov.io/gh/RevolutionTech/django-pigeon/branch/master/graph/badge.svg)](https://codecov.io/gh/RevolutionTech/django-pigeon)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c1add1fd523c4bb48a6e5158cdffa1dd)](https://www.codacy.com/app/RevolutionTech/django-pigeon)

## Installation

```
$ pip install django-pigeon
```

## Usage

django-pigeon comes equipped with a `RenderTestCase` which provides an assortment of methods on top of Django's `TestCase` that assist with end-to-end testing of views in Django. Writing a test that verifies a view renders correctly is as simple as:

```python
from pigeon.test import RenderTestCase


class FooTestCase(RenderTestCase):

    def testFooView(self):
        self.assertResponseRenders('/foo/')
```

You can also inspect the rendered response:

```python
def testFooView(self):
    response = self.assertResponseRenders('/foo/')
    self.assertIn('FOO', response.content)
```

By default, `assertResponseRenders` verifies that the status code of the response is 200, but you can change this by specifying the `status_code` keyword argument:

```python
def testBarView404(self):
    self.assertResponseRenders('/bar/', status_code=404)
```

You can also make POST and PUT requests using `assertResponseRenders` by providing the `method` and `data` keywords arguments:

```python
def testCreateFooView(self):
    payload = {'text': 'Hello World!'}
    self.assertResponseRenders('/foo/create/', status_code=201, method='POST', data=payload)
```

If you are using HTML generated from Django forms, you can set `has_form_error=True` as a shortcut to check for `errorlist` in the resulting HTML:

```python
def testCreateFooViewWithoutText(self):
    response = self.assertResponseRenders('/foo/create/', method='POST', has_form_error=True)
    self.assertIn('This field is required.', response.content)
```

Use `assertAPIResponseRenders` for JSON responses. `json.loads` is automatically called on the response, so the object returned is ready for inspection:

```python
def testFooAPIView(self):
    payload = {'text': 'Hello!'}
    response = self.assertAPIResponseRenders('/foo/', method='POST', data=payload)
    self.assertEquals(response['text'], 'Hello!')
```

You can use `assertResponseRedirects` to test redirects:

```python
def testFooRedirects(self):
    # /foo/ redirects to /bar/
    self.assertResponseRedirects('/foo/', '/bar/')
```

If you have a list of views that you want to verify are rendering as 200 without adding any special assertion logic, you can simply override the `get200s` and `getAPI200s` methods, which should return a list of URLs. django-pigeon will construct test methods that check that rendering all of these URLs results in a 200:

```python
class FooTestCase(RenderTestCase):

    def get200s(self):
        return [
            '/foo/',
            '/bar/',
            '/foobar/',
        ]

    def getAPI200s(self):
        return [
            '/api/foo/',
        ]
```

Most of the features in `RenderTestCase` are actually implemented in the mixin class `RenderTestCaseMixin`. You can combine `RenderTestCaseMixin` with other TestCase classes to get additional functionality:

```python
from django.test import TransactionTestCase
from pigeon.test import RenderTestCaseMixin


class FooTransactionTestCase(RenderTestCaseMixin, TransactionTestCase):

    def testFooView(self):
        ...
```

django-pigeon supports Python 3.5+ and Django 2.2+.
