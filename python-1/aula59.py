# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# desempacotamento em chamadas de funções
for nome in lista:
  print(nome, end=' ')

# OU
  
print(*lista)
print(*string)
print(*tupla)