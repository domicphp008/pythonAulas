Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a =5
>>> b = 4
>>> print(a)
5
>>> print(b)
4
>>> print(a + b)
9
>>> print(a - b)
1
>>> print(a * B)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a * B)
NameError: name 'B' is not defined
>>> print(a * b)
20
>>> print( a / b)
1.25
>>> print(a ** B)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(a ** B)
NameError: name 'B' is not defined
>>> print(a ** b)
625
>>> print(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined
>>> c = a + b
>>> print(c)
9
>>> c = a +  a * b
>>> print(c)
25
>>> c = (a + b) * b
>>> print (c)
36
>>> c = (a + a) *b
>>> print(c)
40
>>> a = 1
>>> b = 2
>>> c = 3
>>> d = b ** b - 4 * a * c
>>> print (d)
-8
>>> 
