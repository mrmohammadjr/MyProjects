def pay(hours,rate):
	if hours <= 40.0: 
		return rate * hours
	overtime = hours - 40.0
	return (rate * 40.0) + (1.5 * rate * overtime)

def checkforfloat(input1):
	try:
		val = float(input1)
		return val
	except ValueError:
		print('Error')
		quit()

inputH = input('Enter Hours: ')
numH = int(inputH)
resultH = checkforfloat(numH)

inputR = input('Enter Rate: ')
numR = int(inputR)
resultR = checkforfloat(numR)
pays = pay(resultH, resultR)
print('Pay: ', pays)