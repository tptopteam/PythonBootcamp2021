Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao = shape.turtle()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tao = shape.turtle()
NameError: name 'shape' is not defined
>>> tao.shape('dog')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.shape('dog')
  File "C:\Users\tptop\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named dog
>>> tao.shape('turtle')
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)

		
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3

>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)
	tao.left(90)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3

>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)
	tao.left(180)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)
	tao.left(135)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(10):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)
	tao.left(36)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่', i)
	tao.left(36)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
8 เหลี่ยมรูปที่ 4
8 เหลี่ยมรูปที่ 5
8 เหลี่ยมรูปที่ 6
8 เหลี่ยมรูปที่ 7
8 เหลี่ยมรูปที่ 8
8 เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> 
>>> def regtangle():
	for i in range(4)
	
SyntaxError: invalid syntax
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	

>>> tao.size('20')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tao.size('20')
AttributeError: 'Turtle' object has no attribute 'size'
>>> 