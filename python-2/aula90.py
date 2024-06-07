import sys

# Generator expression, Interables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
print(next(iterator)) # Eu
print(next(iterator)) # Tenho
print(next(iterator)) # __iter__

# Generator = funções que sabem pausar
lista = [n for n in range(1000)] # valores do iteravel já esta na memória
generator = (n for n in range(1000)) # valores do generator estão esperando para serem acessados

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# OBS -> Não podemos acessar dados diretamente no generator como na lista padrão, ele só sabe o proximo valor ('next')