def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("introduzca un numero: "))
 
if NumeroPerfecto(num):
  print("{} es un numero perfecto" .format(num))
else:
  print("{} NO es un numero perfecto" .format(num))
