# -*- coding: utf-8 -*-
import cgi
import os
class Request(object):

    def __init__(self, env = os.environ):
      self.form = cgi.FieldStorage()
      self.env = env

class Response(object):

    def __init__(self, charset = 'utf-8'):
        self.headers = {'Content-type':'text/html; charset = %s' % charset}
        self.body = ""
        self.status = 200
        self.status_message = ''

    def set_header(self, name, value):
        self.headers[name] = value

    def get_header(self, name):
        return self.headers.get(name, None)

    def set_body(self, bodystr):
        self.body = bodystr

    def make_output(self, timestamp = None):
        import time
        _weekdayname = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        _monthname = [None,
              "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if timestamp is None:
            timestamp = time.time()
            year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
            dtstr="%s, %02d %3s %4d %02d:%02d:%02d GMT" % (
                         _weekdayname[wd], day,
                         _monthname[month], year,
                         hh, mm, ss)
            self.set_header("Last-Modified", dtstr)
            headers = '\n'.join(["%s: %s" % (k, v)
                               for k,v in self.headers.items()])
        return headers + '\n\n' + self.body

    def __str__(self):
        return self.make_output().encode('utf-8')

def get_htmltemplate():
    html_body = u"""
    <html>
      <head>
        <meta http-equiv = "content-type"
              content = "text/html;charset = utf-8" />
      </head>
      <body>
      %s
      </body>
    </html>"""
    return html_body
