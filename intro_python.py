
lista_1 = [10, 20, 30]
lista_1.extend([40, 50, 60]) #Adiciona um valor no final da lista atual
print(lista_1)

lista_1 = [10, 20, 30]
del lista_1[1] # "del" remove um item da lista de acordo com o indice, sempre contando de 0 a 4
print(lista_1)

ista_1 = [10, 20, 30]
50 in lista_1 #verifica se um valor está na lista

lista_1 = [7, 3, 5, 8, 2]
lista_1.reverse() # "reverse"inverte a ordem da lista
lista_1.sort() # "sort" ordena a lista em ordem crescente
print(lista_1)

L = [4, 6, 1, 8, 3]
L.extend([10])
L.sort()
L.reverse()
del L[3]
print(L)

L = [15, 25, 35, 45, 55]
25 in L # "in" verifica se um valor está na lista
50 in L
del L[3]
print(L)

print("LANCHONETE")
print("PRODUTOS","PREÇO")
cardapio = {"Salgado": 4.50, "Lanche": 6.50, "Suco": 3.00, "Refrigerante": 3.50, "Doce": 1.00} #cardapio é um dicionario, que é definido por um conjunto de valores, onde cada valor é associado a uma chave de acesso.
print(cardapio)

N = {"Antônio": 100, "Simon": 90, "Alvin": 0, "Violet": 80, "Theodore": 80}
M = sum(N.values())/len(N)
print("Média da turma:", M)


