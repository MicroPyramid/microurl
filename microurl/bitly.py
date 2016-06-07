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

    def link_edit(self, link, edit, title=None, note=None, private=None, user_ts=None, archived=None):
        params = dict(link=link)
        params['edit'] = edit
        if title:
            params['title'] = title
        if note:
            params['note'] = note
        if private:
            params['private'] = private
        if user_ts:
            params['user_ts'] = user_ts
        if archived:
            params['archived'] = archived
        params['access_token'] = self.access_token
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/link_edit', params)
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

    def highvalue(self, limit=10):
        params = dict(limit=limit)
        params['access_token'] = self.access_token
        response = self.send_request(
            'get', self.ssl_host + 'v3/highvalue', params)
        return response

    def search(self, query, limit=10, offset=0, lang='en', cities=None, domain=None, fields=None):
        params = dict(limit=limit)
        params['offset'] = offset
        params['query'] = query
        params['lang'] = lang
        if cities:
            params['cities'] = cities
        if domain:
            params['domain'] = domain
        if fields:
            params['fields'] = fields

        params['access_token'] = self.access_token
        response = self.send_request('get', self.ssl_host + 'v3/search', params)
        return response

    def bursting_phrases(self):
        params = dict(access_token=self.access_token)
        response = self.send_request(
            'get', self.ssl_host + 'v3/realtime/bursting_phrases', params)
        return response

    def hot_phrases(self):
        params = dict(access_token=self.access_token)
        response = self.send_request(
            'get', self.ssl_host + 'v3/realtime/hot_phrases', params)
        return response

    def clickrate(self, phrase):
        params = dict(access_token=self.access_token)
        params['phrase'] = phrase
        response = self.send_request(
            'get', self.ssl_host + 'v3/realtime/clickrate', params)
        return response

    def link_info(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/info', params)
        return response

    def link_content(self, link, content_type='html'):
        params = dict(access_token=self.access_token)
        params['link'] = link
        params['content_type'] = content_type
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/content', params)
        return response

    def link_category(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/category', params)
        return response

    def link_social(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/social', params)
        return response

    def link_location(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/location', params)
        return response

    def link_language(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/language', params)
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

    def user_networkhistory(self, offset=None, expand_client_id=None, limit=None, expand_user=None):
        params = dict(access_token=self.access_token)
        if offset:
            params['offset'] = offset
        if expand_client_id:
            params['expand_client_id'] = expand_client_id
        if limit:
            params['limit'] = limit
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/network_history', params)
        return response

    def user_tracking_domain_list(self):
        params = dict(access_token=self.access_token)
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/tracking_domain_list', params)
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

    def user_share_counts(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/share_counts', params, **kwargs)
        return response

    def user_share_counts_by_share_type(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/share_counts_by_share_type', params, **kwargs)
        return response

    def user_shorten_counts(self, **kwargs):
        params = dict(access_token=self.access_token)
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/shorten_counts', params, **kwargs)
        return response

    def link_clicks(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/clicks', params, **kwargs)
        return response

    def link_countries(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/countries', params, **kwargs)
        return response

    def link_referrers(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/referrers', params, **kwargs)
        return response

    def link_referrers_by_domain(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/referrers_by_domain', params, **kwargs)
        return response

    def link_referring_domains(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/referring_domains', params, **kwargs)
        return response

    def link_shares(self, link, **kwargs):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/link/shares', params, **kwargs)
        return response

    def link_encoders(self, link, my_network=None, subaccounts=None, limit=None, expand_user=None):
        params = dict(access_token=self.access_token)
        params['link'] = link
        if my_network:
            params['my_network'] = my_network
        if subaccounts:
            params['subaccounts'] = subaccounts
        if limit:
            params['limit'] = limit
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/encoders', params)
        return response

    def link_encoders_by_count(self, link, my_network=None, subaccounts=None, limit=None, expand_user=None):
        params = dict(access_token=self.access_token)
        params['link'] = link
        if my_network:
            params['my_network'] = my_network
        if subaccounts:
            params['subaccounts'] = subaccounts
        if limit:
            params['limit'] = limit
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/encoders_by_count', params)
        return response

    def link_encoders_count(self, link):
        params = dict(access_token=self.access_token)
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/link/encoders_by_count', params)
        return response

    def bundle_archive(self, bundle_link):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/archive', params)
        return response

    def bundles_by_user(self, user, expand_user=None):
        params = dict(access_token=self.access_token)
        params['user'] = user
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/bundles_by_user', params)
        return response

    def bundle_clone(self, bundle_link):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/clone', params)
        return response

    def bundle_collaborator_add(self, bundle_link, collaborator):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['collaborator'] = collaborator
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/collaborator_add', params)
        return response

    def bundle_collaborator_remove(self, bundle_link, collaborator):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['collaborator'] = collaborator
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/collaborator_remove', params)
        return response

    def bundle_contents(self, bundle_link, expand_user=None):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/contents', params)
        return response

    def bundle_create(self, private=None, title=None, description=None):
        params = dict(access_token=self.access_token)
        if private:
            params['private'] = private

        if title:
            params['title'] = title
        if description:
            params['description'] = description
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/create', params)
        return response

    def bundle_edit(self, bundle_link, edit=None, private=None, title=None, description=None, preview=None, og_image=None):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        if edit:
            params['edit'] = edit
        if private:
            params['private'] = private
        if title:
            params['title'] = title
        if description:
            params['description'] = description
        if preview:
            params['preview'] = preview
        if og_image:
            params['og_image'] = og_image

        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/edit', params)
        return response

    def bundle_link_add(self, bundle_link, link, title=None):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link

        if title:
            params['title'] = title

        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_add', params)
        return response

    def bundle_link_comment_add(self, bundle_link, link, comment):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link

        params['comment'] = comment

        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_comment_add', params)
        return response

    def bundle_link_comment_edit(self, bundle_link, link, comment_id, comment):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        params['comment_id'] = comment_id
        params['comment'] = comment
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_comment_edit', params)
        return response

    def bundle_link_comment_remove(self, bundle_link, link, comment_id):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        params['comment_id'] = comment_id

        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_comment_remove', params)
        return response

    def bundle_link_edit(self, bundle_link, link, edit, title=None, preview=None):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        params['edit'] = edit

        if title:
            params['title'] = title

        if preview:
            params['preview'] = preview

        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_edit', params)
        return response

    def bundle_link_remove(self, bundle_link, link):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_remove', params)
        return response

    def bundle_link_reorder(self, bundle_link, link, display_order):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        params['display_order'] = display_order
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/link_reorder', params)
        return response

    def bundle_pending_collaborator_remove(self, bundle_link, collaborator):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['collaborator'] = collaborator
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/pending_collaborator_remove', params)
        return response

    def bundle_reorder(self, bundle_link, link):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        params['link'] = link
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/reorder', params)
        return response

    def bundle_view_count(self, bundle_link):
        params = dict(access_token=self.access_token)
        params['bundle_link'] = bundle_link
        response = self.send_request(
            'get', self.ssl_host + 'v3/bundle/view_count', params)
        return response

    def user_bundle_history(self, expand_user=None):
        params = dict(access_token=self.access_token)
        if expand_user:
            params['expand_user'] = expand_user
        response = self.send_request(
            'get', self.ssl_host + 'v3/user/bundle_history', params)
        return response

    def bitly_pro_domain(self, domain):
        params = dict(access_token=self.access_token)
        params['domain'] = domain
        response = self.send_request(
            'get', self.ssl_host + 'v3/bitly_pro_domain', params)
        return response

    def user_tracking_domain_clicks(self, domain, **kwargs):
        params = dict(access_token=self.access_token)
        params['domain'] = domain
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/tracking_domain_clicks', params, **kwargs)
        return response

    def user_tracking_domain_shorten_counts(self, domain, **kwargs):
        params = dict(access_token=self.access_token)
        params['domain'] = domain
        response = self.send_metrics_request(
            'get', self.ssl_host + 'v3/user/tracking_domain_shorten_counts', params, **kwargs)
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

        # params = urllib.parse.urlencode(params)
        # info = urllib.request.urlopen(
        #     "https://api-ssl.bitly.com/oauth/access_token", params)
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
        auth = "Basic " + base64.b64encode(username + ":" + password)
        headers = dict(Authorization=auth)
        params.update({'format': 'json'})
        kw = dict(params=params, headers=headers)

        response = requests.request(
            'POST', 'https://api-ssl.bitly.com/oauth/access_token', **kw)

        response = str(response.text)
        return response
