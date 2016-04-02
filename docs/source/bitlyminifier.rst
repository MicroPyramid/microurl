===============
Bitly Minifier
===============

----------------------------
1. Authentication for bitly
----------------------------

.. code-block:: python

    from microurl import bitlyauthentication

    authentication = bitlyauthentication(client_id, client_secret, redirect_uri)

    auth_url=authentication.authorization_url()

open auth_url in your browser.After authorizing app, you will be redirected to redirect_url with code perameter.

.. code-block:: python

    access_token=authentication.get_accesstoken_from_code(code) # code that you get to redirect_url in the above step


----------------------------------------------
2. Authentication using username and password
----------------------------------------------

.. code-block:: python

    access_token=authentication.get_accesstoken_from_username_pwd(bitlyusername or login email,password)


------------
Basic Usage
------------

**Function definitions (i.e. shorturl()) can be found by reading over microurl/bitly.py**

.. code-block:: python

    from microurl import bitlyapi

    bitly=bitlyapi(access_token) # access_token is getting from previous steps

    minified=bitly.shorturl(longurl,domain)['url'] # domain is optional here


**To get detail information of bitlylink.**

.. code-block:: python

    bitly.url_info(bitlylink,expand_user='True | False',hash='one or more bitly hashes') # expand_user,hash are optional here


**To get the number of clicks on a single bitly link.**

.. code-block:: python

    bitly.link_clicks(bitlylink, unit="day", units=10, timezone=-4, limit=20, unit_reference_ts="now")

    # here except bitlylink all are optional

**To get the number of shares on a single bitly link.**

.. code-block:: python

    bitly.link_shares(bitlylink, unit="day", units=10, timezone=-4, limit=20, unit_reference_ts="now")

    # here except bitlylink all are optional


**To get loggedin user info**

.. code-block:: python

    bitly.user_info()


**To get user link history in reverse chronological order.**

.. code-block:: python

    bitly.user_linkhistory(bitlylink, limit=20, offset=1, created_after='1381000000', created_before='1381844314', expand_client_id=True, archived="both", private="both")

    # here all fields are optional
