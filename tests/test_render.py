from http import HTTPStatus

from pigeon.test import RenderTestCase


class RenderFooTestCase(RenderTestCase):
    def get200s(self):
        return [
            "/foo/",
        ]

    def getAPI200s(self):
        return [
            "/api/foo/",
        ]

    def testFooViewReturnsHelloWorld(self):
        response = self.assertResponseRenders("/foo/")
        self.assertIn(b"Hello World!", response.content)

    def testPostFooAPIViewReturns204(self):
        self.assertAPIResponseRenders(
            "/api/foo/",
            status_code=HTTPStatus.NO_CONTENT,
            method="POST",
            data={"text": "Hello World!"},
        )

    def testBarRedirectsToFoo(self):
        self.assertResponseRedirects("/bar/", "/foo/")
