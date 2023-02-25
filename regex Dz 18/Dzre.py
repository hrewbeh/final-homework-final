import re

userTime = input('time')

times = re.findall(r'[0-2][0-9]\:[0-5][0-9]',userTime)

if times == [] or int(times[0][0]) == 2 and int(times[0][1]) > 3:
	print('Время указано неправильно')
else:
	print(times[0])

userColor = input('color')
maxi = [0-9]
colorrgb = re.search(r'rgb\([0-9]+,[0-9]+,[0-9]+\)',userColor.lower())
colorhex = re.findall(r'#[A-Fa-f0-9]{6}',userColor)
try:
	colorrgb = colorrgb.group()
	colo = re.findall(r'[0-9]+', colorrgb)
	if int(max(colo)) > 255 or int(min(colo)) < 0:
		print('Ввели не rgb')
	elif colorhex == []:
		print(colorrgb,'Hex HE HAIDEH')
	else:
		print(colorrgb,colorhex)
except AttributeError:
	print('RGB не найдено')



userVEKA = input('century')

century = re.findall(r'^(X{0,3}|XL|L|LX|LXX|XC)?(I{0,3}|IV|V|VI|VII|VIII|IX)$',userVEKA)
print(century[0][0] + century[0][1])
