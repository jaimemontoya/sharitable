#!"C:\Python27\python.exe"
#Some code from:
#https://github.com/pgbovine/csc210-fall-2015/blob/master/www/cgi-bin/lecture4-query-database.py
#https://github.com/pgbovine/csc210-fall-2015/blob/master/www/cgi-bin/lecture4.py

print "Content-Type: text/html"
print # don't forget the extra newline	

import sqlite3
conn = sqlite3.connect('donors.db')
c = conn.cursor()

import json
data = {}
#data = {'name':'Kasun', 'address':'columbo','age': '29'}
#data['myName'] = 'Jaime'
#data['myLastName'] = 'Montoya'

for r in c.execute('SELECT typeid, typename FROM type;'):
  # r[0] corresponds to typeid. r[1] corresponds to typename.
  data[r[0]] = r[1]




print json.dumps(data)
