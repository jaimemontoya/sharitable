#!"C:\Python27\python.exe"

#Some code from:
#https://github.com/pgbovine/csc210-fall-2015/blob/master/www/cgi-bin/lecture4-query-database.py
#https://github.com/pgbovine/csc210-fall-2015/blob/master/www/cgi-bin/lecture4.py

# print the http header
#stuff from lecture4.py

#this is for sign-up! 

print "Content-Type: text/html"
print # don't forget the extra newline

import cgi
form = cgi.FieldStorage()
userValue = form['usernameValue'].value
passwordVal = form['passwordValue'].value 
zipVal = form['zipcodeValue'].value
addressVal = form['addressValue'].value

import sqlite3
conn = sqlite3.connect('donors.db')
c = conn.cursor()

import json

#data = "hello"
#print json.dumps("hello")
data = {}
#for r in c.execute('select username from users where username="emichel2";'):
#	data = r
	
found = 0	
for r in c.execute('select username from users where username=?;',[userValue]):	
	found = 1

if found == 1:
	data = "already there"
else:
	data = "sucessfully added"
	c.execute('insert into users values (?, ?, ?, ?)', (userValue, passwordVal, addressVal, zipVal))

conn.commit()
print json.dumps(data)
