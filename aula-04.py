Python 3.4.4rc1 (v3.4.4rc1:04f3f725896c, Dec  6 2015, 16:42:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 'hello'
>>> y = 42
>>> z = 'there'
>>> 
>>> print(x +z)
hellothere
>>> print x,y)
SyntaxError: Missing parentheses in call to 'print'
>>> print (x,y)
hello 42
>>> print(+y)
42
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(x+y)
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> print(x+str(y))
hello42
>>> 
>>> print(x, y, z)
hello 42 there
>>> 
