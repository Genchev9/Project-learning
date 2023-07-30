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
      self.list2=[random.randint(0,0) for i in range(self.z)]
      self.list3.append(self.list2)
  def generate(self,lownumber,highnumber):
    self.lownumber=lownumber
    self.highnumber=highnumber
    self.list3=[]
    for self.list2 in range(self.u):
      self.list2=[random.randint(self.lownumber,self.highnumber) for o in range(self.z)]
      self.list3.append(self.list2)
  def display(self):
    for x in self.list3:
      print(x,sep='\n')
  def count(self):
    print(f'количество строк: {self.u},количество столбцов: {self.z}')
  def replace(self,m,n,q): # первый агрумент номер сторки второй аргумент номер в строке третий аргумент значение которое надо подставить 
    try:
      self.q=q
      self.m=m
      self.n=n
      self.list3[self.m].pop(self.n)
      self.list3[self.m].insert(self.n,self.q)
    except:
      print('значение за границой матрицы')
p=Matrix(5,7)
p.display()
p.generate(10,15)
p.display()
p.generate(-10,10)
p.display()
p.count()
p.replace(1,2,111)
p.display()