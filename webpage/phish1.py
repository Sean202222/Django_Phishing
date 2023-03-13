import cgi
data = cgi.FieldStorage()

list = '<ul>'

if data.getvalue('sender'):
    list += '<li>' + data.getvalue('sender')
    
if data.getvalue('main'):
    list += '<li>' + data.getvalue('main')
    
if data.getvalue('date'):
    list += '<li>' + data.getvalue('date')
    
if data.getvalue('link'):
    list += '<li>' + data.getvalue('link')
    
list = '</ul>'