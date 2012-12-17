# -*- coding: utf-8 -*-
import requests


class Proxy(object):

    default_options = dict(verify=False, allow_redirects=False)

    def __init__(self, url, **kwargs):
        self.url = url.rstrip('/')
        options = self.default_options.copy()
        options.update(kwargs)
        self.options = options

    def __call__(self, environ, start_response):
        kwargs = self.options.copy()
        headers = []
        for k, v in environ.items():
            if k[:5] == 'HTTP_':
                headers.append((k[5:].replace('_', '-').title(), v))
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        headers.append(('Content-Length', content_length))
        kwargs['headers'] = headers

        if content_length:
            kwargs['data'] = environ['wsgi.input'].read(content_length)

        content_type = environ.get('CONTENT_TYPE')
        if content_type and content_type is not None:
            headers.append(('Content-Type', content_type))

        path = environ['PATH_INFO']
        if environ.get('QUERY_STRING'):
            path += '?' + environ.get('QUERY_STRING')

        meth = getattr(requests, environ['REQUEST_METHOD'].lower())
        resp = meth(self.url + path, **kwargs)

        headers = [(k.title(), v) for k, v in resp.headers.items()]

        start_response('%s %s' % (resp.status_code, resp.reason), headers)
        return resp.iter_content()
