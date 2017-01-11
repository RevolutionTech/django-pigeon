from pigeon.test import RenderTestCase


class RenderFooTestCase(RenderTestCase):

    def get200s(self):
        return [
            '/foo/',
        ]

    def testFooViewReturnsHelloWorld(self):
        response = self.assertResponseRenders('/foo/')
        self.assertIn(b'Hello World!', response.content)

    def testFooAPIView(self):
        self.assertAPIResponseRenders('/api/foo/')

    def testPostFooAPIViewReturns204(self):
        self.assertAPIResponseRenders('/api/foo/', status_code=204, method='POST', data={'text': 'Hello World!'})

    def testBarRedirectsToFoo(self):
        self.assertResponseRedirects('/bar/', '/foo/')
