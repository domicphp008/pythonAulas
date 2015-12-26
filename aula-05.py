Python 3.4.4rc1 (v3.4.4rc1:04f3f725896c, Dec  6 2015, 16:42:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = '42'
>>> type(x)
<class 'str'>
>>> y = 3
>>> type(y)
<class 'int'>
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x+y)
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> int(x) + y
45
>>> x + str(y)
'423'
>>> 
