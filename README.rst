microurl
========
python library for url minification.

Features
--------
- Google
    - URL Minifier
- Bitly
    - URL Minifier
- Supr
    - URL Minifier


Installation
------------

Install microurl via `pip <http://www.pip-installer.org/>`_

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

Basic Usage
-----------

**Function definitions (i.e. google_mini()) can be found by reading over microurl/google.py**

.. code-block:: python
    
    minified = google_mini('validurl', 'Google_API_KEY')

its as simple as that.


Questions, Comments, etc?
-------------------------

Our hope is that microurl is so simple that you'd never *have* to ask any questions, but if you feel the need to contact us for this (or other) reasons, you can hit us up at micropyramid@googlegroups.com.


Want to help?
-------------

microurl is useful, but ultimately only as useful as the people using it (say that ten times fast!). If you'd like to help, write example code, contribute patches, document things on the wiki, tweet about it. Your help is always appreciated!
