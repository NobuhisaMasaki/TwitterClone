#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()
import datetime

form_body = u"""
               <h2>Twitter Clone!</h2>
               <h3>New tweet</h3>
               <form method = "POST" action = "/cgi-bin/index.py">
                 <input type = "text" name = "author" required placeholder = "Your Name"/>
                 <input type = "text" name = "body"   required placeholder = "Tweet"/>
                 <input type = "submit" />
               </form>
               <h3>New Arrival</h3>
           """
list = u"""
          <div style = "padding: 5px; margin: 5px; border-radius: 5px; background-color: lightblue">
            <div style = "padding: 5px; margin: 5px; border-radius: 5px; background-color: white">
              %s
            </div>
            <span style = "font-size: 8px">
              by %s,
            </span>
            <span style = "font-size: 8px">
              at %s
            </span>
          </div>
        """

con = sqlite3.connect('./dbfile.dat')
cur = con.cursor()
try:
    cur.execute("CREATE TABLE tweet (author text, body text, time date);")
except:
    pass

content = ""
req = Request()
if req.form.has_key('body'):
    cur.execute("INSERT INTO tweet(author, body, time) VALUES('%s', '%s', '%s')" % (req.form.getvalue('author'), req.form.getvalue('body'), str(datetime.datetime.now())))

cur.execute("SELECT * FROM tweet ORDER BY time DESC")
for res in cur.fetchall():
    body   = res[1]
    author = res[0]
    time   = res[2]
    content += list % (body, author, time)

con.commit()
res = Response()
body = form_body + content
res.set_body(get_htmltemplate() % body)
print res
