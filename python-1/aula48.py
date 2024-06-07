'''
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, 
  extend - estende a lista
  + - concatena listas

Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD) 
'''
import os

os.system('cls')
#   +01234
#   -54321
string = 'ABCDE'
lista_vazia = []# criando uma lista VAZIA => ''

#         0    1           2          3   4
lista = [123, True, 'Matheus Braga', 1.2, []] 
#print(lista, type(lista))

print(lista_vazia)
print(lista)

lista_exemplo = [10, 20, 30, 40, 50] # lista de tamanho 5, com 5 valores int
lista_exemplo[2] = 300 # update de um valor na lista
del lista_exemplo[2] #'del' exclue um dado da lista
print(lista_exemplo) # le o valor da lista

lista_exemplo.append(60) # 'append' adiciona um valor para a lista na última posição
lista_exemplo.append(80)
lista_exemplo.append('Matheus')
lista_exemplo.append(90)
print(lista_exemplo)
ultimo_valor = lista_exemplo.pop() # remove o último valor da lista e retorna o valor
print(lista_exemplo, 'Removido,', ultimo_valor)

print()

lista_exemplo.clear() # limpa a lista

lista_exemplo.insert(0, 1) # escolhe a posição na lista e insere um valor => no caso posição = 0, valor = 1
lista_exemplo.insert(1, 2)
lista_exemplo.insert(2, 3)
lista_exemplo.insert(3, 4)
print(lista_exemplo)

print()

# CONCATENANDO STRINGS
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b 

print(lista_c)

lista_d = lista_a.extend(lista_b) #OBS: 'EXTEND' não retorna valores para atribuir em outras variáveis, sempre vai ser 'None'
print(lista_d)

# o 'extend' sempre vai corrigir a lista diretamente
lista_a.extend(lista_b)
print(lista_a)

print()

'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista_a = ['Matheus', 'Arthur']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa' # o print da lista 'a' muda também pois o valor foi substituido no mesmo espaço da memória da máquina
print(lista_a) 
print(lista_b)

print()

lista_a = ['Matheus', 'Arthur']
lista_b = lista_a.copy() # utilizamos copy para mandar um resultado copiado para a outra variável

lista_a[0] = 'Qualquer coisa'
print(lista_a) 
print(lista_b)