import json

from django.test import TestCase, TransactionTestCase

from pigeon.url.utils import strip_params_from_url, add_params_to_url


class RenderTestCaseMeta(type):

    def __new__(cls, name, bases, dct):
        def testRender200s(self):
            for url in self.get200s():
                self.assertResponseRenders(url)

        if 'get200s' in dct:
            dct['testRender200s'] = testRender200s
        return type.__new__(cls, name, bases, dct)


class RenderTestCaseMixin(object):

    __metaclass__ = RenderTestCaseMeta

    def assertResponseRenders(self, url, status_code=200, method='GET', data={}, has_form_error=False, **kwargs):
        request_method = getattr(self.client, method.lower())
        follow = status_code == 302
        response = request_method(url, data=data, follow=follow, **kwargs)

        if status_code == 302:
            redirect_url, response_status_code = response.redirect_chain[0]
        else:
            response_status_code = response.status_code
        self.assertEquals(
            response_status_code,
            status_code,
            "URL {url} returned with status code {actual_status} when {expected_status} was expected.".format(
                url=url,
                actual_status=response_status_code,
                expected_status=status_code
            )
        )

        # Check that forms submitted did not return errors (or did if it should have)
        form_error_assertion_method = self.assertIn if has_form_error else self.assertNotIn
        form_error_assertion_method('errorlist', response.content)

        return response

    def assertAPIResponseRenders(self, url, status_code=200, method='GET', data={}, **kwargs):
        api_url = add_params_to_url(url, {'format': 'json'})
        if data:
            data = json.dumps(data)
        response = self.assertResponseRenders(
            api_url,
            status_code=status_code,
            method=method,
            data=data,
            content_type='application/json',
            **kwargs
        )
        if status_code in [
            204,  # No Content
            205,  # Reset Content
        ]:
            return response
        return response.json()

    def assertResponseRedirects(self, url, redirect_url, status_code=200, method='GET', data={}, **kwargs):
        response = self.assertResponseRenders(url, status_code=302, method=method, data=data, **kwargs)
        redirect_url_from_response, _ = response.redirect_chain[0]
        self.assertEquals(strip_params_from_url(redirect_url_from_response), redirect_url)
        self.assertEquals(response.status_code, status_code)


class RenderTestCase(RenderTestCaseMixin, TestCase):
    pass


class RenderTransactionTestCase(RenderTestCaseMixin, TransactionTestCase):
    pass
