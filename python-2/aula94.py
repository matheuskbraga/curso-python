# try, except, else e finally
try: 
  print('ABRIR ARQUIVO')
except ZeroDivisionError: # tratar o erro, quantos except eu quiser
  print('DIVIDIU ZERO')
else: 
  print('Não deu erro')
finally: # sempre irá executar com o try, independente de ter erro ou não
  print('FECHAR ARQUIVO')