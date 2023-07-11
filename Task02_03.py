number_1={0:'zero',1:'one',2:'two',3:'three',4:'fouth',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
def switch_it_up(number):
    try:
      print(f'{number_1[number]}')
    except:
      print('none')
switch_it_up(5)