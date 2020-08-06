#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print() # 한줄 띄워야 해서 들어가는 것임
