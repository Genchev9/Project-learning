monts={1:'январь. 31 дней',2:'февраль. 28 дней',3:'март. 31 дней',4:'апрель. 30 дней',5:'май. 31 дней',6:'июнь. 30 дней',7:'июль. 31 дней',8:'август. 31 дней',9:'сентбятрь. 30 дней',10:'октябрь. 31 дней',11:'ноябрь. 30 дней',12:'декабрь. 31 дней'}
def monts_1(mont):
    if mont<=12:
        print('вы ввели',monts[mont])
    else:
      print('Такого месяца нет!')    
monts_1(11)
monts_1(1)
monts_1(13)