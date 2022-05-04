# O  CODIGO ABAIXO LÊ BASE E ALTURA DE UM RETANGULO
# E RETORNA A ÁREA,PERIMETRO E DIAGONAL COM 4 CASAS DECIMAIS
import math

B = float(input("Base do retangulo:"))
H = float(input("Altura do retangulo:"))
area = B*H
perimetro = (2*B)+(2*H)
diagonal = math.sqrt((pow(B,2)+pow(H,2)))

print(f'AREA = {area:,.4f}')
print(f'PERIMETRO = {perimetro:,.4f}')
print(f'DIAGONAL = {diagonal:,.4f}')
