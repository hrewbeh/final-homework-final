more_num = input("Введите несколько 3 значения чисел через пробел\n").split()
how_action = input("Cложить или Умножить?(Выбери 1 если сложить или 2 если умножить)\n")
if how_action == "1":
	print(int(more_num[0]) + int(more_num[1]) + int(more_num[2]))
elif how_action == "2":
	print(int(more_num[0]) * int(more_num[1]) * int(more_num[2]))
else:
	print("Вы ввели не то Попробуйте снова")
	
print('Это конец первого')

three_num = input('Введите 3 числа\n').split()
user_choice = input('Выбери 1 ели нужно вывести максимум, 2 если минимум, 3 если среднее арифметическое\n')
if user_choice == '1':
	print(max(three_num))
elif user_choice == '2':
	print(min(three_num))
elif user_choice == '3':
	print((int(three_num[0]) + int(three_num[1]) + int(three_num[2])) / len(three_num))
else:
	print("вы ввели не то Попробуйте снова")

print("Это конец второго")

distance_in_metr = int(input('Введите колличество метров которое мы с вами переведем\n'))
user_choise2 = input('1 - Мили, 2 - Дюймы, 3 - Ярды\n')
if user_choise2 == '1':
	print(round(distance_in_metr * 0.000621371, 3), "Миль")
elif user_choise2 == '2':
	print(round(distance_in_metr * 39.3701, 3), "Дюймов")
elif user_choise2 == '3':
	print(round(distance_in_metr * 1.09361), "Ярдов")
else:
	print("Вы ввели не то Попробуйте снова")
	
	
	
	
	
	
	
	
	
	
	
	
	