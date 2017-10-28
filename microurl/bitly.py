import requests
import base64


class bitlyapi(object):

    def __init__(self, access_token):
        self.host = 'https://api.bit.ly/'
        self.ssl_host = 'https://api-ssl.bit.ly/'
        self.access_token = access_token

    def shorturl(self, url, preferred_domain=None):
        params = dict(longUrl=url)
        if preferred_domain:
            params['domain'] = preferred_domain
        params['access_token'] = self.access_token
        response = self.send_request('get', self.ssl_host + 'v3/shorten', params)
        return response

    def expand(self, url):
        params = dict(shortUrl=url)
        params['access_token'] = self.access_token
        response = self.send_request('get', self.ssl_host + 'v3/expand', params)
        return response

    def url_info(self, url, bitly_hash=None, expand_user=None):
        params = dict(shortUrl=url)
        if bitly_hash:
            params['hash'] = bitly_hash
        if expand_user:
            params['expand_user'] = expand_user
        params['access_token'] = self.access_token
        response = self.send_request('get', self.ssl_host + 'v3/info', params)
        return response

    def link_lookup(self, url):
        params = dict(url=url)
        params['access_token'] = self.access_token
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/lookup', params)

        return response

    def user_link_lookup(self, url):
        params = dict(url=url)
        params['access_token'] = self.access_token
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/link_lookup', params)
        return response

    def user_link_save(self, longUrl, title=None, note=None, private=None, user_ts=None):
        params = dict(longUrl=longUrl)
        params['access_token'] = self.access_token
        if title:
            params['title'] = title
        if note:
            params['note'] = note
        if private:
            params['private'] = private
        if user_ts:
            params['user_ts'] = user_ts
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/link_save', params)
        return response

    def link_info(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/info', params)
        return response

    def app_details(self, client_id):
        params = dict(access_token=self.access_token)
        params['client_id'] = client_id
        response = self.send_request(
            'get', self.ssl_host + 'v3/oauth/app', params)
        return response

    def user_info(self, login=None, full_name=None):
        params = dict(access_token=self.access_token)
        if login:
            params['login'] = login

        if full_name:
            params['full_name'] = self.full_name
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/info', params)
        return response

    def user_linkhistory(
            self, link=None, limit=None, offset=None, created_before=None,
            created_after=None, modified_after=None, expand_client_id=None,
            archived=None, private=None, user=None):

        params = dict(access_token=self.access_token)
        if link:
            params['link'] = link
        if offset:
            params['offset'] = offset
        if created_before:
            params['created_before'] = created_before
        if created_after:
            params['created_after'] = created_after
        if modified_after:
            params['modified_after'] = modified_after
        if expand_client_id:
            params['expand_client_id'] = expand_client_id
        if archived:
            params['archived'] = archived
        if private:
            params['private'] = private
        if user:
            params['user'] = user
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/link_history', params)
        return response

    def user_clicks(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/clicks', params, **kwargs)
        return response

    def user_countries(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/countries', params, **kwargs)
        return response

    def user_popular_links(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/popular_links', params, **kwargs)
        return response

    def user_referrers(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/referrers', params, **kwargs)
        return response

    def user_referring_domains(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/referring_domains', params, **kwargs)
        return response

    def user_shorten_counts(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/shorten_counts', params, **kwargs)
        return response

    def bitly_pro_domain(self, domain):
        params = dict(access_token=self.access_token)
        params['domain'] = domain
        response = self.send_request(
            'get', self.ssl_host + 'v3/bitly_pro_domain', params)
        return response

    def send_request(self, method, url, params=None, headers=None, timeout=60):
        if params is None:
            params = dict(format='json')
        else:
            params.update({'format': 'json'})

        if headers is None:
            headers = {}

        kw = dict(params=params, headers=headers, timeout=timeout)

        response = requests.request(method.upper(), url, **kw)
        response = response.json()
        if 'data' in response:
            response = response['data']
        return response

    def send_metrics_request(self, method, url, params, unit=None, units=None, timezone=None, rollup=None, limit=None, unit_reference_ts=None):

        if unit:
            params['unit'] = unit
        if units:
            params['units'] = units
        if timezone:
            params['timezone'] = timezone
        if rollup:
            params['rollup'] = rollup
        if limit:
            params['limit'] = limit
        if unit_reference_ts:
            params['unit_reference_ts'] = unit_reference_ts

        response = self.send_request(method, url, params)
        return response


class bitlyauthentication(object):

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.host = 'https://bitly.com/oauth/'

    def authorization_url(self):
        rty = self.host + "authorize?client_id=" + self.client_id
        rty += "&redirect_uri=" + self.redirect_uri
        self.auth_url = rty
        return rty

    def get_accesstoken_from_code(self, code):
        params = {}
        params['grant_type'] = 'authorization_code'
        params['code'] = code
        params['redirect_uri'] = self.redirect_uri
        params['client_id'] = self.client_id
        params['client_secret'] = self.client_secret
        info = requests.post('https://api-ssl.bitly.com/oauth/access_token', params=params)
        info = str(info.text)
        info = info.split('=')
        info = info[1].split('&')
        access_token = info[0]
        self.access_token = access_token
        return access_token

    def get_accesstoken_from_username_pwd(self, username, password):

        params = dict(client_id=self.client_id)
        params['client_secret'] = self.client_secret
        auth = "Basic " + str(base64.b64encode((username + ":" + password).encode('ascii')))
        headers = dict(Authorization=auth)
        params.update({'format': 'json'})
        kw = dict(params=params, headers=headers)

        response = requests.request(
            'POST', 'https://api-ssl.bitly.com/oauth/access_token', **kw)

        response = str(response.text)
        return response
