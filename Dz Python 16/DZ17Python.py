#1
revers = input('Пользователь вводит с клавиатуры строку\n')
print(revers[::-1])

#3
useinp = input('Пользователь вводит с клавиатуры строку')
userinp2 = input('и символ для поиска')

knives = len([x for x in useinp if x == userinp2])

print('сколько раз в строке встречается искомый символ:',knives)

#5
useinp = input('Пользователь вводит с клавиатуры строку')
userinp2 = input('слово для поиска')
useinp3 = input(', слово для замены')

print(useinp.replace(userinp2,useinp3))

#4
import re

useinp = input('Пользователь вводит с клавиатуры строку')
userinp2 = input('слово для поиска')

fnaf = re.findall(userinp2,useinp)

print(len(fnaf))

#2

useinp = input('Пользователь вводит с клавиатуры строку')

print('Колличество цифр:',len([i for i in useinp if i.isdigit()]),
      'Count bukv:',len([i for i in useinp if i.isalpha()]))






