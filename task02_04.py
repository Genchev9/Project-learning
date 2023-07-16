def remove(arr):
  if arr[-1]=='!':
    arr_1=arr[:-1]
    print(arr_1)
  else:
    print(arr)
remove('Hi!!!')
def remove_1(arr):
  arr_2=arr.replace('!','')
  print(arr_2)
remove_1('!@hel!oo!!') 