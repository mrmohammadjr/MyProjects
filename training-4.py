#example 1
def test() :
	print('hello')
print('hi')
test()
#example 2
big = max('rasooli')
print(big)
small = min('rasooli')
print(small)
#example 3
x = 10

def text():
	print('this is a simple code')
x += 2
print(x)
text()
#example 4
def fname(name):
	print('hello ' + name)
fname('javad')
#example 5
def intnum(num):
	if num == 10 :
		print('number is 10')
	elif num == 20 :
		print('number is 20')
	else :
		print('number is 30')
intnum(30)
#example 6
def test2():
	return 'test2'
print(test2())
#example 7
def intnum2(num2):
	if num2 == 10 :
		return 'number is 10'
	elif num2 == 20 :
		return 'number is 20'
	else :
		return 'number is 30'
print(intnum2(10))
#example 8
def twonum(m,j,r):
	sum = m + j + r
	return sum
result = twonum(10,20,30)
print(result)