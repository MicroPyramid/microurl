import urllib2
import json
from conf import Google_API_KEY

# This will minify url using google url minifier and return minified url
def google_mini(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key='+Google_API_KEY
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = urllib2.Request(
        post_url,
        json.dumps(postdata),
        headers
    )
    ret = urllib2.urlopen(req).read()
    return json.loads(ret)['id']


# This will stats of the minified url using google url shortner
def google_stat(min_url)
    pass


# This will minify url using bily
def bitly_mini(url)
    pass
