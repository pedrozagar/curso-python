while True:
    try:
        valor1 = int(input("digite o primeiro valor: "))
        break
    except ValueError:
        print("valor invalido! favor digite um numero inteiro.")
        exit(1)
    except KeyboardInterrupt:
        print("\noperacao cancelada pelo usuario.")
        exit(1)

while True:
    try:
        valor2 = int(input("digite o primeiro valor: "))
        break
    except ValueError:
        print("valor invalido! favor digite um numero inteiro.")
        exit(1)
    except KeyboardInterrupt:
        print("\noperacao cancelada pelo usuario.")
        exit(1)

valor1 = int(input("digite o primeiro valor: "))
valor2 = int (input("digite o segundo valor: "))
print("selecione uma opcao: ")
print("1 - adicao")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")

while True:
    try:
        opcao = int(input("digite a opcao desejada: "))
        break
    except ValueError:
        print("")

opcao = int(input("digite a opcao desesjada: "))

resultado = None #None = nada ou null. foi criado variável com valor de nada para a variável do resultado no final existir. se for 0 seria algo mas aqui eu só preciso de algo para existir e assim não der bug no final.

match opcao:
    case 1:
        resultado = valor1 + valor2
    case 2:
        resultado = valor1 - valor2
    case 3:
        resultado = valor1 * valor2
    case 4:
        resultado = valor1 / valor2
    case _:
        print("opcao invalida!")
if resultado is not None:
        print("resultado: ", resultado)
