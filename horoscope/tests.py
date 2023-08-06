from django.test import TestCase


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        responce = self.client.get('/horoscope/')
        self.assertEqual(responce.status_code, 200)

    def test_libra(self):
        responce = self.client.get('/horoscope/libra/')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('Libra is the seventh sign of the zodiac, planet Venus (September 24 to October 23).',
                      responce.content.decode())
    def test_libra_redirect(self):
        responce = self.client.get('/horoscope/7/')
        self.assertEqual(responce.status_code,302)
        self.assertEqual(responce.url, '/horoscope/libra/')

    def test_aries(self):
        responce = self.client.get('/horoscope/aries/')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('Aries is the first sign of the zodiac, planet Mars (March 21 to April 20).',
                      responce.content.decode())
    def test_aries_redirect(self):
        responce = self.client.get('/horoscope/1/')
        self.assertEqual(responce.status_code,302)
        self.assertEqual(responce.url, '/horoscope/aries/')

