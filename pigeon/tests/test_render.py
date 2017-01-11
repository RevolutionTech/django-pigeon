from pigeon.test import RenderTestCase


class RenderFooTestCase(RenderTestCase):

    def testFooViewReturnsHelloWorld(self):
        response = self.assertResponseRenders('/foo/')
        self.assertIn('Hello World!', response.content)
