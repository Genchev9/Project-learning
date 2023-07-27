import random as random
u=int(input("введите количество столбцов"))
z=int(input("введите длину строки"))
list3=[]
for list2 in range(u):
  list2=[random.randint(1,10) for i in range(z)]
  list3.append(list2)
print(list3)