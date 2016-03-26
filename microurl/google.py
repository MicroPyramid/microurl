import json
import requests


def google_mini(url, Google_API_KEY):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + \
        Google_API_KEY
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return json.loads(r.text)['id']


def google_expand(short_url, Google_API_KEY):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + \
        Google_API_KEY
    payload = {'shortUrl': short_url}
    r = requests.get(post_url, params=payload)
    return r.json()['longUrl']


def qrcode(url):
    return 'http://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=' + url
