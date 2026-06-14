vendas = 2000 #ou 800

#if = se as vendas forem maiores que 1000, mostra "ganhou bônus"
if vendas > 1000:
    print("ganhou bônus")
else:
    print("não ganhou bônus")
#else = caso as vendas forem menores que 800, mostra "não ganhou bônus"

print()

print("mostre os valores ou os nomes dos produtos:")
listaProdutos = ["iphone", "ipad", "notebook"] #aqui eu criei uma variável chamada listaProdutos
listaPrecos = [1500, 5000, 5500]

#for = executa um comando várias vezes
#o for aqui para este comando todo abaixo está dizendo: "para cada produto dentro da lista de produtos, exibe os produtos para mim"
for valores in listaPrecos:
    print(valores * 2)

print()

#for i é especial = ele executa x vezes que eu peço ali dentro do parênteses
for i in range(3):
    print("não sou um robô")

print()

print("exemplos de quebra de espaço:")
print("\nolá")

#se eu quiser deixar tudo como anotação precisa ser três aspas ou uma aspa normal: 
# """
# aqui o texto 
# aqui o texto
# """
#ou
#'''
#teste
#teste
#'''