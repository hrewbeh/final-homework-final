while True:
    from random import randint
    print('Я не понял задание поэтому сделаем все наоборот.\nВы вводите стоимость звонка, '
          'с помощью рандома определим стоимость минуты \nи я выведу колличество минут которое укладывается в ваш бюджет ')
    prick_heroin = int(input("Че по бабкам\n"))
    picki_pack = prick_heroin / randint(0, 10)
    def abc(num):
        try:
            int(picki_pack)
            return int(picki_pack)
        except ValueError:
            return picki_pack
    print(f'{abc(picki_pack)} Минут')