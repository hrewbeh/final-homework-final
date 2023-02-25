while True:
	try:
		user_inp = int(input('Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.\n'))
	except ValueError:
		user_inp = int(input('Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.\n'))
	if user_inp % 3 ==0 and user_inp % 5 != 0 and user_inp > 1 and user_inp <= 100:
		print('Fizz')
	elif user_inp % 3 != 0 and user_inp % 5 == 0 and user_inp > 1 and user_inp <= 100:
		print('Buzz')
	elif user_inp % 3 == 0 and user_inp % 5 == 0 and user_inp > 1 and user_inp <= 100:
		print('Fizz Bizz')
	elif user_inp % 3 != 0 and user_inp % 5 != 0 and user_inp > 1 and user_inp <= 100:
		print(user_inp)
	else:
		print(' сообщение об ошибке')
		
# Тут нужно ограничить ввод в инпуте не прибегая к (and user_inp > 1 and user_inp <= 100)  и пересдать