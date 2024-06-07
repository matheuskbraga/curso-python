# dir, hasattr e getattr em Python -> CHECAR MÉTODOS DENTRO OBJETOS QUALQUER
string = 'Matheus'

# OBS: O NOME DO MÉTODO VEM COMO 'STRING'
if hasattr(string, 'upper'): # existe upper aqui ??? 
  print('Existe upper')
  print(string.upper())

metodo = 'upper'

if hasattr(string, metodo): # existe upper aqui ???
  print('Existe upper')
  print(string.upper())

print()
print('-------------------------')
print()

