#example 1
x = 5
if x > 20 :
	print('x is bigger than 20')
if x < 10 :
	print('x is smaller than 10')
#example 2
for y in range(5):
	print(y)
	if y > 20 :
		print('y is bigger than 20')
	if y < 10 :
		print('y is smaller than 10')
#example 3
z = 10
if z > 9 :
	print('z is bigger than 9')
	if z < 20 :
		print('z is smaller than 20')
print('all done')
#example 4
a = 10
if a > 20 :
	print('true')
else :
	print('false')
#example 5
b = 20
if b > 30 :
	print('b is bigger than 30')
elif b == 20 :
	print('b is equal to 20')
else :
	print('b is small')
print('done')
#example 6
c = 30
if c > 40 :
	print('c is bigger than 40')
elif c > 20 :
	print('c is bigger than 20')
#example 7
d = 40
if d < 30 :
	print('d is smaller than 30')
elif d >= 40 :
	print('d is equal to 40')
else :
	print('error')
#example 8
txt = 'hello'
try :
	num = int(txt)
except :
	num = 'false'
print('this code is ' + num)
#example 9
input1 = input('enter number :')
try :
	intnum = int(input1)
except :
	intnum = -1
if intnum > 0 :
	print('this code is true')
else :
	print('not a number')
#example 10