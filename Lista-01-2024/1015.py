'''
*DISTÂNCIA ENTRE DOIS PONTOS*
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
 p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após
a vírgula, segundo a fórmula:

Distancia = https://resources.beecrowd.com/gallery/images/problems/UOJ_1015.png

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de
ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o 
ponto decimal.
'''
x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

distancia = (x2-x1)**2 + (y2-y1)**2
raiz = distancia ** 0.5

print(f"{raiz:.4f}")
