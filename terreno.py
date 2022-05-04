# o codigo abaixo coleta do usuario as medidas do terreno
# e o valor do m² ,e retorna a área e o valor do terreno

largura=float(input("digite a largura do terreno:"))
comprimento=float(input("digite o comprimento do terreno:"))
valorm=float(input("digite o valor do m²:"))
area=largura*comprimento
preço=valorm*area
print("Area do terreno ="+str(area))
print("Preço do terreno ="+"R$ "+str(preço))
