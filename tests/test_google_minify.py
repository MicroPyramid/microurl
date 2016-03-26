import unittest
from microurl.google import google_mini

GOOGLE_API_KEY = 'AIzaSyB_nDH7Uvm6-KSbsJD_OqYXA2XmuZ1P1lE'

WRONG_GOOGLE_API_KEY = 'testwrongapikey'

class TestGoogleKey(unittest.TestCase):

    def test_wrong_google_key(self):
        with self.assertRaises(KeyError):
            google_mini('https://micropyramid.com/', WRONG_GOOGLE_API_KEY)

    def test_correct_google_key(self):
        result = google_mini('https://micropyramid.com/', GOOGLE_API_KEY)
        self.assertTrue(result)


class Testwrongurl(unittest.TestCase):

    def test_wrong_url(self):
        with self.assertRaises(KeyError):
            google_mini('wrong urlpattern', GOOGLE_API_KEY)

if __name__ == '__main__':
    unittest.main()
