==============
requests_proxy
==============

A WSGI Proxy using `requests <http://docs.python-requests.org/>`_.


Installation
============

With pip::

  $ pip install requests_proxy

Usage
=====

Create a proxy::

  >>> from requests_proxy import Proxy
  >>> proxy = Proxy(application_url)

Then use it. Here is an example with WebOb but you can use it like a classic
WSGI application::

  >>> from webob import Request
  >>> req = Request.blank('/form.html')
  >>> resp = req.get_response(proxy)
  >>> print(resp.text)
  <html>...
  ...</html>

The Proxy application accept some keyword arguments. Those arguments are passed
to requests during the process.  By default ``allow_redirects`` and ``verify``
are set to ``False`` but you can change the behavior::

  >>> proxy = Proxy(application_url, verify=True, allow_redirects=True,
  ...               max_redirects=10)

Warning
=======

This proxy does not totally respect the RFC. Chunked Transfer-Encoding in
request headers are not supported. Also if you plan to upload some large file,
the proxy is not able to stream the content. (Mostly because requests is not
able to stream requests' body)

If you need a more robust WSGI proxy, have a look at
`restkit.contrib.wsgi_proxy
<https://github.com/benoitc/restkit/blob/master/restkit/contrib/wsgi_proxy.py>`_


