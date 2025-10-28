import sys

print("Nome do script: ", sys.argv[0])
print("Parametros: ", sys.argv[1:])
 
servidor = sys.argv[1]
user = sys.argv[2]
password = "*****"

print(f'O servidor é {servidor} o user é {user} e a pass é {password}')
