from django.test import TestCase

# Create your tests here.

class TestMain(TestCase):

    def test_main_tab(self):
        responce = self.client.get('')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('Horoscope app', responce.content.decode())
        self.assertIn('Apps', responce.content.decode())
        self.assertIn('Main', responce.content.decode())
