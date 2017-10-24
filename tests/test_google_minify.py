import unittest
from microurl.google import google_mini, google_expand

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


class TestMinifyAndExpand(unittest.TestCase):

    def test_minify_and_expand(self):
        test_url = 'https://micropyramid.com/'

        minified_url = google_mini(test_url, GOOGLE_API_KEY)
        self.assertTrue(minified_url)

        expanded_url = google_expand(minified_url, GOOGLE_API_KEY)
        self.assertEqual(test_url, expanded_url)


if __name__ == '__main__':
    unittest.main()
