#se eu quero saber se um valor é positivo ou negativo:

valor = int(input("digite um valor: "))
if(valor >= 0):
	print("positivo")
else:
	print("negativo")
	
#como se usa o IF:

valor = int(input("digite um valor: "))
if(valor >= 0):
	print("positivo")
elif(valor < 0):
	print("negativo")
else:
    print("nulo")