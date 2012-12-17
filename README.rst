==============
requests_proxy
==============

A WSGI Proxy using `requests <http://docs.python-requests.org/>`_.


Installation
------------

With pip::

  $ pip install requests_proxy

Usage
-----

Create a proxy::

  >>> from requests_proxy import Proxy
  >>> proxy = Proxy(application_url)

Then use it. Here is an example with WebOb but you can use it like a classic WSGI application::

  >>> from webob import Request
  >>> req = Request.blank('/form.html')
  >>> resp = req.get_response(proxy)
  >>> print(resp.text)
  <html>...
  ...</html>
