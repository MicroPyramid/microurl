import json
import requests


def google_mini(url, Google_API_KEY):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + \
        Google_API_KEY
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        return r.json().get('id')
    elif r.status_code == 400:
        raise KeyError('Can not Generate Minified url, Reason:', r.json().get('error', {}).get('errors')[0].get('reason'))
    raise KeyError('Invalid Google Api Key or url')
