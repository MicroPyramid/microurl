================
Google Minifier
================

First, you'll want to head over to google or bily or supr and register an application!

After you register, grab your applications ``Consumer Key`` and ``Consumer Secret`` from the application details tab.

First, you'll want to import your desired minfier from microurl

.. code-block:: python

    from microurl import google_mini


------------
Basic Usage
------------

**Function definitions (i.e. google_mini()) can be found by reading over microurl/google.py**

.. code-block:: python

    minified = google_mini('validurl', 'Google_API_KEY')

its as simple as that.


-------------
QR Generator
-------------

.. Code-block:: python

    qr_url = qrcode(url)
