monts_1={1:'январь',2:'февраль',3:'март',4:'апрель',5:'май',6:'июнь',7:'июль',8:'август',9:'сентбятрь',10:'октябрь',11:'ноябрь',12:'декабрь'}
def quarter_of(months):
    if months>=1 and months<=3:
        print(f'месяц {months} {monts_1[months]} являеться частью первого квартала')
    elif months>=4 and months<=6:
      print(f'месяц {months} {monts_1[months]} являеться частью второго квартала')
    elif months>=7 and months<9:
      print(f'месяц {months} {monts_1[months]} являеться частью трейтего квартала')
    elif months>=10 and months<=12:
      print(f'месяц {months} {monts_1[months]} являеться частью четветого квартала')
quarter_of(11)