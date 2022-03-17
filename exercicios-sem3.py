'''
    Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.
'''
# numeros = []

# for i in range(10):
#     numeros.append(i+1)

# print(numeros)

# for numero in numeros:
#     if (numero % 2 == 0):
#         print('O número ' + (str(numero)) + ' É par..')
#     else:
#         print('O número ' + (str(numero)) + ' É ímpar..')

'''
    Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.
'''
# frase = input('Escreva uma frase qualquer..\n')
# consoantes = ''
# for letra in frase:
#     if (letra.lower() not in 'aeiou'):
#         consoantes += letra
# print(consoantes)

'''
    Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10, no formato:
'''
# numero = 0
# tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while True:
#     try:
#         numero = int(input('Digite um número\n'))
#         break
#     except ValueError:
#         print('Número inválido')

# print('Tabuada do', numero)
# for exp in tabuada:
#     print('{} x {} = {}'.format(numero, exp, numero * exp))

'''
    Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente. A saída do programa deve ser o resultado da operação: numerador elevado ao expoente. Observação: não usar função interna que calcula automaticamente potência.
'''
# while True:
#     try:
#         numerador = int(input('Digite um número..'))
#         expoente = int(input('Digite um expoente..'))
#         break
#     except ValueError:
#         print('Digite um número válido')

# op = numerador ** expoente

# print('Operação: {} elevado a {} = {}'.format(numerador, expoente, op))

'''
    Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".
'''
# while True:
#     try:
#         login = str(input('Insira o seu nome de usuário:\n'))
#         password = str(input('Insira a sua senha:\n'))
#         if (login == password):
#             print('Seus dados de login e senha são inválidos, insira novamente as suas informações de login')
#         else:
#             break
#     except ValueError:
#         print('Seus dados de login e senha são inválidos, insira novamente as suas informações de login')
# print('Bem-vindo ao Sistema!')

'''
    Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média dos números informados.
'''
# contador = 0
# soma = 0
# while True:
#     num = int(input("Digite um número (0 para encerrar): "))
#     if num == 0:
#         break
#     else:
#         contador += 1
#         soma += num
# if contador == 0:
#     print("Não foram inseridos números a calcular.")
# else:
#     media = soma / contador
#     print("A média dos", contador, "números é", media)

'''
    Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio), seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados. Ao final da compra, deve ser informado o valor total do pedido.
'''
print("Sistema de compras")
total = 0
continuar = True
while continuar:
    while True:
        produto = input("Informe o nome do produto a ser comprado: ")
        if produto != "":
            break
        else:
            print("Nome do produto inválido.")
    while True:
        try:
            valor = float(input("Informe o valor unitário do produto: "))
            if valor <= 0:
                print("O valor do produto deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Valor do produto inválido.")
    while True:
        try:
            quant = int(input("Informe a quantidade do produto a ser comprada: "))
            if valor <= 0:
                print("O valor do produto deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Valor do produto inválido.")

    total += quant * valor

    resp = input("Produto inserido com sucesso. Deseja comprar mais algum produto (s/n)? ")
    if resp == "n":
        continuar = False
print(f"Valor total da compra: R$ {total:.2f}")