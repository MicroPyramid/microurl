import unittest
from microurl.bitly import bitlyapi, bitlyauthentication

BITLY_ACCESS_TOKEN = '948f673940a8a91636dbb980d2e6be3060920465'
CLIENT_ID = '461701c1b925d403fa802dff3b61d0bf34e80934'
REDIRECT_URI = "http://micropyramid.mt.io:8000"
CLIENT_SECRET = "9c656680c74cf70920101eb661d26e696137f3df"


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
        a = bitly.shorturl(url=url)
        self.assertTrue(a)

    def test_expand(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        short_url = bitly.expand(url=url)
        self.assertTrue(short_url)

    def test_app_details(self):
        bitly = self.get_bitly()
        client_id = "461701c1b925d403fa802dff3b61d0bf34e80934"
        response = bitly.app_details(client_id=client_id)
        self.assertTrue(response)

    def test_url_info(self):
        bitly = self.get_bitly()
        url = "http://micropyramid.com"
        bitly_hash = "12345"
        expand_user = "abcd"
        short_url = bitly.url_info(url=url, expand_user=expand_user, bitly_hash=bitly_hash)
        self.assertTrue(short_url)

    def test_link_lookup(self):
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
        link = "http://micropyramid.com"
        result = bitly.link_info(link=link)
        self.assertFalse(result)

    def test_user_info(self):
        bitly = self.get_bitly()
        result = bitly.user_info("abcd")
        self.assertTrue(result)

    def test_user_linkhistory(self):
        bitly = self.get_bitly()
        link = "http://micropyramid.com"
        limit = "12345"
        offset = "offset"
        created_before = 1900
        created_after = 122
        modified_after = 100
        expand_client_id = "461701c1b925d403fa802dff3b61d0bf34e80934"
        archived = False
        private = False
        # user = "dateofbirth"
        result = bitly.user_linkhistory(link=link,
                                        limit=limit,
                                        offset=offset,
                                        created_before=created_before,
                                        created_after=created_after,
                                        modified_after=modified_after,
                                        expand_client_id=expand_client_id,
                                        archived=archived,
                                        # user=user,
                                        private=private)
        self.assertTrue(result)

    def test_user_clicks(self):
        bitly = self.get_bitly()
        response = bitly.user_clicks()
        self.assertTrue(response)

    def test_user_countries(self):
        bitly = self.get_bitly()
        response = bitly.user_countries()
        self.assertTrue(response)

    def test_user_popular_links(self):
        bitly = self.get_bitly()
        response = bitly.user_popular_links()
        self.assertTrue(response)

    def test_user_referrers(self):
        bitly = self.get_bitly()
        response = bitly.user_referrers()
        self.assertTrue(response)

    def test_user_referring_domains(self):
        bitly = self.get_bitly()
        response = bitly.user_referring_domains()
        self.assertTrue(response)

    def user_shorten_counts(self):
        bitly = self.get_bitly()
        response = bitly.user_shorten_counts()
        self.assertTrue(response)

    def test_bitly_pro_domain(self):
        bitly = self.get_bitly()
        domain = "abcd.com"
        response = bitly.bitly_pro_domain(domain=domain)
        self.assertTrue(response)


class TestBitlyAuthentication(unittest.TestCase):

    def get_bitly(self):
        bitly = bitlyauthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
        return bitly

    def test_bitly_authentication(self):
        bitly = self.get_bitly()
        self.assertTrue(bitly)

    def test_get_accesstoken_from_username_pwd(self):
        bitly = self.get_bitly()
        username = "dateofbirth"
        password = "navi@123"
        response = bitly.get_accesstoken_from_username_pwd(
            username=username,
            password=password
        )
        self.assertTrue(response)

    # def test_get_accesstoken_from_code(self):
    #     bitly = self.get_bitly()
    #     authentication = bitlyauthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    #     auth_url = authentication.authorization_url()
    #     print(auth_url)
    #     code = 'd6ab04f6f268e6656f98f9d707757e87a596c1c2'
    #     response = bitly.get_accesstoken_from_code(
    #         code=code,
    #     )
    #     self.assertTrue(response)

    def test_authorization_url(self):
        bitly = self.get_bitly()
        response = bitly.authorization_url()
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
