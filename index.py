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
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action = '''
    <form action="process_delete.py" method="post">
      <input type="hidden" name="pageId" value="{}">
      <input type="submit" value="delete">  
    </form> 
  '''.format(pageId)
else:
  pageId = 'Welcome'
  description = 'Hello, web'
  update_link = ''
  delete_action = ''
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
  {update_link}
  {delete_action}
  <h2> {title} </h2>
  <p> {desc} </p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))
