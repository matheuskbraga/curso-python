import os

os.system('cls')
lista = []

while True:
  print('Selecione uma das opções')
  opcao = input('[i]nserir [a]pagar [l]istar: ')  

  if opcao == 'i':
    os.system('cls')
    valor = input('Valor: ')
    lista.append(valor)

  elif opcao == 'a':
    os.system('cls')
    indice_str = input('Escolha o índice para apagar: ')
    try:
      indice = int(indice_str)
      del lista[indice]
    except:
      print('Este índice não está na lista')

  elif opcao == 'l':
    os.system('cls')
    if len(lista) == 0:
      print('Nada para listar')
    for i, valor in enumerate(lista):
      print(i, valor)
