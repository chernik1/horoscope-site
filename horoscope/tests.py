from django.test import TestCase


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        responce = self.client.get('/horoscope/')
        self.assertEqual(responce.status_code, 200)
        self.assertIn('Horoscope main', responce.content.decode())
        self.assertIn('<h1>Horoscope apps</h1>', responce.content.decode())


class TestZodiacs(TestCase):
    def test_libra(self):
        responce = self.client.get('/horoscope/libra')
        self.assertEqual(responce.status_code, 301)

    def test_libra_redirect(self):
        responce = self.client.get('/horoscope/7')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/7/')

    def test_aries(self):
        responce = self.client.get('/horoscope/aries')
        self.assertEqual(responce.status_code, 301)

    def test_aries_redirect(self):
        responce = self.client.get('/horoscope/1')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/1/')

    def test_taurus(self):
        responce = self.client.get('/horoscope/taurus')
        self.assertEqual(responce.status_code, 301)

    def test_taurus_redirect(self):
        responce = self.client.get('/horoscope/2')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/2/')

    def test_gemini(self):
        responce = self.client.get('/horoscope/gemini')
        self.assertEqual(responce.status_code, 301)

    def test_gemini_redirect(self):
        responce = self.client.get('/horoscope/3')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/3/')

    def test_cancer(self):
        responce = self.client.get('/horoscope/cancer')
        self.assertEqual(responce.status_code, 301)

    def test_cancer_redirect(self):
        responce = self.client.get('/horoscope/4')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/4/')

    def test_leo(self):
        responce = self.client.get('/horoscope/leo')
        self.assertEqual(responce.status_code, 301)

    def test_leo_redirect(self):
        responce = self.client.get('/horoscope/5')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/5/')

    def test_virgo(self):
        responce = self.client.get('/horoscope/virgo')
        self.assertEqual(responce.status_code, 301)

    def test_virgo_redirect(self):
        responce = self.client.get('/horoscope/6')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/6/')

    def test_scorpio(self):
        responce = self.client.get('/horoscope/scorpio')
        self.assertEqual(responce.status_code, 301)

    def test_scorpio_redirect(self):
        responce = self.client.get('/horoscope/8')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/8/')

    def test_sagittarius(self):
        responce = self.client.get('/horoscope/sagittarius')
        self.assertEqual(responce.status_code, 301)

    def test_sagittarius_redirect(self):
        responce = self.client.get('/horoscope/9')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/9/')

    def test_capricorn(self):
        responce = self.client.get('/horoscope/capricorn')
        self.assertEqual(responce.status_code, 301)

    def test_capricorn_redirect(self):
        responce = self.client.get('/horoscope/10')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/10/')

    def test_aquarius(self):
        responce = self.client.get('/horoscope/aquarius')
        self.assertEqual(responce.status_code, 301)

    def test_aquarius_redirect(self):
        responce = self.client.get('/horoscope/11')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/11/')

    def test_pisces(self):
        responce = self.client.get('/horoscope/pisces')
        self.assertEqual(responce.status_code, 301)

    def test_pisces_redirect(self):
        responce = self.client.get('/horoscope/12')
        self.assertEqual(responce.status_code, 301)
        self.assertEqual(responce.url, '/horoscope/12/')

