'''
*SEIS NÚMEROS ÍMPARES*
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir
de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
'''
num = int(input())

if num%2 == 0:
  num += 1

for impar in range(num, num + 12, 2):
  print(impar)
