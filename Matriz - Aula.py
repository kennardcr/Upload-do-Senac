#print("\n--------------------- EXEMPLO 1 ---------------------\n")

# matriz = [
#     [5, 8, 2],
#     [7, 3, 9],
#     [4, 6, 1],
# ]
# print(matriz[0][2])
# print("O [0] REPRESENTA A LINHA E O [2] REPRESENTA A COLUNA... IGUAL AO EXCEL - A3")

#print("\n--------------------- EXEMPLO 2 ---------------------\n")

# matriz = [
#     [10, 20],
#     [30, 40],
# ]
# matriz[0][1]=[99]
# print(matriz)
# print("SUBSTITUI O 20, PELO 99")

#print("\n--------------------- EXEMPLO 3 ---------------------\n")

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60]
# ]

# for numero in matriz[0]:
#     print(numero)
#     print("RETORA AS COLUNAS DA LINHA 1 DA MATRIZ... RETORNA NA POSIÇÃO VERTICAL - 1 POR LINHA")

# for linha in matriz:
#     print(linha)
#     print("RETORNA TODA A MATRIZ, NO MESMO LAYOUT DA MATRIZ")

# for linha in matriz:
#     for numero in linha:
#         print(numero)
#         print("RETORNA TODA A MATRIZ EM UMA ÚNICA COLUNA, MAS CADA VALOR EM UMA LINHA")

#O i = LINHA
#O j = COLUNA
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j])
#         print("MESMA COISA DO CÓDIGO ANTERIOR, MAS É MELHOR PARA ESPECIFICAÇÃO ENTRE LINHA E COLUNA, PARA RETORNO DA RESPOSTA CORRETA")
        
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print("Linha:", i)
#         print("Coluna:", j)
#         print("Valor:", matriz[i][j])
#         print("RETORNA CADA ENDEREÇAMENTO DA CÉLULA DA MATRIZ. VALOR É O NÚMERO QUE CONSTA NAQUELA POSIÇÃO")
        
        
#print("\n--------------------- EXEMPLO 4 ---------------------\n")

# matriz = []

# for i in range(2):
#     linha = []
#     for j in range(2):
#         numero = int(input("Digite um número: "))
#         linha.append(numero)
#     matriz.append(linha)
# print("Estas informações foram inseridas na matriz!")

# ver = input("\nDeseja ver a sua matriz? (sim/não): ")
# if ver == "sim":
#     for linha in matriz:
#         print(linha)
# else:
#     print("Tudo bem!")

# # soma = 0
# # for linha in matriz:
# #     for numero in linha:
# #         soma += numero
# # print(f"\nObs: A soma total destes números é igual a: {soma}\n")

# for linha in matriz:
#     for numero in linha:
#         if numero % 2 == 0:
#             print(numero)

# quantidade = 0
# for linha in matriz:
#     for numero in linha:
#         if numero % 2 == 0:
#             quantidade += 1
# print(f"\nA quantidade de n° pares nesta matriz é igual a: {quantidade}\n")

# maior = matriz[0][0]                
# for linha in matriz:
#     for numero in linha:
#         if numero > maior:
#             maior = numero
# print(f"\nO maior numero do matriz é: {numero}\n")

# # soma = 0
# # for numero in matriz[0]:
# #     soma += numero
# # print("A soma da primeira linha é:", soma)

# soma = 0
# for i in range(len(matriz)):
#     soma += matriz[i][0]
# print("A soma da primeira coluna é:", soma)