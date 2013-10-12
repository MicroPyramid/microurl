import urllib2
import json
from conf import Google_API_KEY

def google(url):
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
