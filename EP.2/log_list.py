Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> garage[0]
'toyota'
>>> garage[-1]
'suzuki'
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzuki']
>>> garage[0] = 'suzuki'
>>> garage[-1] = 'toyota'
>>> print(garage)
['suzuki', 'izusu', 'toyota']
>>> top = garage[0]
>>> print(top)
suzuki
>>> garage[-1] = 'suzuki'
>>> garage[0] = 'toyota'
>>> garage.insert(1,'benz')
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> garage.insert(2,'izusu')
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzuki']
>>> garage.remove('izusu')
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> print(garage)
['toyota', 'benz']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> users.sort()
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(revers=True)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    users.sort(revers=True)
TypeError: 'revers' is an invalid keyword argument for sort()
>>> users.sort(reverse=True)
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users,reverse=True))
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in users:
	users.reverse()
	print(u)

	
p
r
b
b
r
p
>>> for u in users:
	print(u.reverse())

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(u.reverse())
AttributeError: 'str' object has no attribute 'reverse'
>>> for u in users:
	print(sorted(u,reverse=True))

	
['p']
['n']
['b']
['t']
['r']
['z']
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in sorted(users,reverse=True):
	print(u)

	
z
t
r
p
n
b
>>> users.reverse()
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+ u)

	
สวัสดี z
สวัสดีz
สวัสดี r
สวัสดีr
สวัสดี t
สวัสดีt
สวัสดี b
สวัสดีb
สวัสดี n
สวัสดีn
สวัสดี p
สวัสดีp
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+  u)

	
สวัสดี z
สวัสดีz
สวัสดี r
สวัสดีr
สวัสดี t
สวัสดีt
สวัสดี b
สวัสดีb
สวัสดี n
สวัสดีn
สวัสดี p
สวัสดีp
>>> 