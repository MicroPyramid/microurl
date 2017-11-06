.. image:: https://readthedocs.org/projects/microurl/badge/?version=latest
    :target: http://microurl.readthedocs.io/en/latest/?badge=latest
.. image:: https://img.shields.io/pypi/v/microurl.svg
    :target: https://pypi.python.org/pypi/microurl
.. image:: https://travis-ci.org/MicroPyramid/microurl.svg?branch=master
    :target: https://travis-ci.org/MicroPyramid/microurl
.. image:: https://coveralls.io/repos/github/MicroPyramid/microurl/badge.svg?branch=master
    :target: https://coveralls.io/github/MicroPyramid/microurl?branch=master
.. image:: https://img.shields.io/pypi/l/microurl.svg
    :target: https://pypi.python.org/pypi/microurl/

python library for url minification.


Features
--------
- Google
    - URL Minifier
    - QR Generator
- Bitly
    - URL Minifier


Installation
------------

Install microurl via `pip <https://pypi.python.org/pypi/microurl/>`_

.. code-block:: bash

    $ pip install microurl

Or, if you want the code that is currently on GitHub

.. code-block:: bash

    git clone git://github.com/micropyramid/microurl.git
    cd microurl
    python setup.py install


Starting Out
------------

First, you'll want to head over to google or bily or supr and register an application!

After you register, grab your applications ``Consumer Key`` and ``Consumer Secret`` from the application details tab.

First, you'll want to import your desired minfier from microurl

.. code-block:: python

    from microurl import google_mini


Basic Usage Of Google Mini
--------------------------

**Function definitions (i.e. google_mini()) can be found by reading over microurl/google.py**

.. code-block:: python

    minified = google_mini('validurl', 'Google_API_KEY')

its as simple as that.


QR Generator
-------------

.. Code-block:: python

    qr_url = qrcode(url)


Authentication for bitly
------------------------

.. code-block:: python

    from microurl import bitlyauthentication

    authentication = bitlyauthentication(client_id, client_secret, redirect_uri)

    auth_url=authentication.authorization_url()

open auth_url in your browser.After authorizing app, you will be redirected to redirect_url with code perameter.

.. code-block:: python

    access_token=authentication.get_accesstoken_from_code(code) # code that you get to redirect_url in the above step


Authentication using username and password
------------------------------------------

.. code-block:: python

    access_token=authentication.get_accesstoken_from_username_pwd(bitlyusername or login email,password)


Basic Usage of Bitly
--------------------

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


Questions, Comments, etc?
-------------------------

https://github.com/MicroPyramid/microurl/issues


Want to help?
-------------

microurl is useful, but ultimately only as useful as the people using it (say that ten times fast!). If you'd like to help, write example code, contribute patches, document things on the wiki, tweet about it. Your help is always appreciated!


For more Updates
----------------
https://micropyramid.com/oss/

Visit our Python Development page `Here`_

We welcome your feedback and support, raise github ticket if you want to report a bug. Need new features? `Contact us here`_

.. _contact us here: https://micropyramid.com/contact-us/
.. _Here: https://micropyramid.com/python-development-services/
