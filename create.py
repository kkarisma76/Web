#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
print("content-type:text/html; charset=utf-8")
print() # 한줄 띄워야 해서 들어가는 것임
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
  
form = cgi.FieldStorage()
if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId, 'r').read()
else:
  pageId = 'Welcome'
  description = 'Hello, web'
print('''<!DOCTYPE html>
<html>
<head>
  <title> Title_WEB </title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py"> WEB </a></h1>
  <ul>
    {listStr}
  </ul>
  <a href="create.py"> CREATE </a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="5" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
