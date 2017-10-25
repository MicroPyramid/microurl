import unittest
from microurl.bitly import bitlyapi

BITLY_ACCESS_TOKEN = '948f673940a8a91636dbb980d2e6be3060920465'


class TestBitly(unittest.TestCase):

    def get_bitly(self):
        bitly = bitlyapi(BITLY_ACCESS_TOKEN)
        return bitly

    def test_bitly(self):
        bitly = self.get_bitly()
        self.assertTrue(bitly)

    def test_shorturl(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        domain = "mp.com"
        bitly.shorturl(url=url, preferred_domain=domain)
        # self.assertTrue(short_url)

    def test_expand(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.shorturl(url=url)
        self.assertTrue(short_url)

    def test_url_info(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.url_info(url=url)
        self.assertTrue(short_url)

    def test_link_lookup(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.link_lookup(url=url)
        self.assertTrue(short_url)

    def test_link_edit(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.link_lookup(url=url)
        self.assertTrue(short_url)

    def test_user_link_lookup(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.user_link_lookup(url=url)
        self.assertTrue(short_url)

    def test_user_link_save(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        title = "micropyramid"
        note = "Pyhon devlopment"
        private = "only organization"
        ts = 'tech'
        result = bitly.user_link_save(longUrl=url,
                                      title=title,
                                      note=note,
                                      private=private,
                                      user_ts=ts)
        self.assertTrue(result)

    def test_link_info(self):
        bitly = self.get_bitly()
        result = bitly.link_info("http://kjlssjd1sd.com")
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()
