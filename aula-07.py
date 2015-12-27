Python 3.4.4rc1 (v3.4.4rc1:04f3f725896c, Dec  6 2015, 16:42:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> 
>>> x = 'hello'
>>> y = 'world'
>>> 
>>> print(x, y)
hello world
>>> 
>>> import math
>>> print('O valor de PI é aproximadamente %5.3f' % math.pi)
O valor de PI é aproximadamente 3.142
>>> 
>>> for x in range(1,11):
	print(x, x**x, end='')
	print(x*x*x)

	
1 11
2 48
3 2727
4 25664
5 3125125
6 46656216
7 823543343
8 16777216512
9 387420489729
10 100000000001000
>>> 
