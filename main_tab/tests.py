from django.test import TestCase

# Create your tests here.

class TestMain(TestCase):

    def test_main_tab(self):
        responce = self.client.get('')
        self.assertEqual(responce.status_code, 200)
