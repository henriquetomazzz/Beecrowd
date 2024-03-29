'''
*NÚMEROS POSITIVOS*
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos 
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''
count = 0
for positivo in range(6):
  valor = float(input())

  if valor > 0:
    count += 1

print(f"{count:.0f} valores positivos")