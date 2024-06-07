'''
WHILE/ELSE
'''

string = 'Valor qualquer'

i = 0
while i < len(string): # se o valor da len(string) for maior que 'i' então é TRUE e o while é executado
  letra = string[i]

  print(letra)
  i += 1
else:
  print('O else foi executado')
print('Fora do while')
print('Tipo: ', type(len(string)))