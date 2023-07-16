def max_min(arr_3):
  n=len(arr_3)
  for i in range(n-1):
    for j in range(n-i-1):
      if arr_3[j]>arr_3[j+1]:
        arr_3[j],arr_3[j+1]=arr_3[j+1],arr_3[j]
  print(f'наименьшее {arr_3[0]} наибольшее {arr_3[-1]}')