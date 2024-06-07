'''
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - tira os espaços vazios no início e no fim das frases cortadas
'''
import os

os.system('cls')
frase = 'Olha só, que coisa interessante'
lista_frases_cruas = frase.split() # separa a frase pelos 'SPACES'
print(lista_frases_cruas)
print('-----------------------------------')
lista_frases_cruas = frase.split(',') # separa a frase pela ','
print(lista_frases_cruas)
print('-----------------------------------')
lista_frases = [] # lista
for i, frase in enumerate(lista_frases_cruas):
  lista_frases.append(lista_frases_cruas[i].strip()) # adiciona as frases separadas na lista 'lista_frase'
print(lista_frases)
print('-----------------------------------')
frases_unidas = ', '.join(lista_frases) # vou unir as frases da 'lista frase' e acrescento uma vírgula + space (, ) entre elas 
print(frases_unidas)