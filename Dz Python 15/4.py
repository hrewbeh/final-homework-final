while True:
	userFour = input("lvl продаж for three менеджеров через space\n").split()
	
	
	def foo(num):
		if int(num) < 500:
			return int(num) / 100 * 3
		elif int(num) >= 500 and int(num) < 1000:
			return int(num) / 100 * 5
		elif int(num) >= 1000:
			return int(num) / 100 * 8
	
	
	one_slave = 200 + foo(userFour[0])
	two_slave = 200 + foo(userFour[1])
	three_slave = 200 + foo(userFour[2])
	if one_slave > two_slave and one_slave > three_slave:
		one_slave += 200
	elif two_slave > one_slave and two_slave > three_slave:
		two_slave += 200
	elif three_slave > one_slave and three_slave > two_slave:
		three_slave += 200
	mass = {'one_slave': one_slave, 'two_slave': two_slave, 'three_slave': three_slave}
	print('Зарплата с учетом премии:', mass)
