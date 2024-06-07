# Exemplo de uso dos sets
import os

os.system('cls')
letras = set()

while True:
  letra = input('Digite uma letra: ')
  letras.add(letra)

  if 'l' in letras:
    print('PARABÉNS')
    break

  print(letras)