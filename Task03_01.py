import random as random
#u=int(input("введите количество столбцов"))
#z=int(input("введите длину строки"))
#list3=[]
#for list2 in range(u):
  #list2=[random.randint(1,10) for i in range(z)]
  #list3.append(list2)
#print(list3)
class Matrix: 
  def __init__(self,u,z):
    list3=[]
    self.list3=list3
    self.u=u
    self.z=z
    for self.list2 in range(self.u):
      self.list2=[random.randint(1,11) for i in range(self.z)]
      self.list3.append(self.list2) 
  def display(self):
    for x in self.list3:
      print(x,sep='\n')      
  def count(self):
    print(f'количество строк: {self.z},количество столбцов: {self.u}')
p=Matrix(5,7)
p.display()
p.count()