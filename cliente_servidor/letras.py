import time 
nome = str(input('Digete seu nome completo: ')).strip()
print('Analizando seu nome... ')
time.sleep(2)
print(f'Seu nome em MAIUSCULA!  e  ({nome.upper()}) ')#upper deixa tudo em MAIUSCULAS 
time.sleep(2) 
print(f'Seu nome em meniscula e {nome.lower()}')#lowe deixa as estrigs em minuscolas
time.sleep(2)
print(f'Seu nome tem au todo {len(nome)- nome.count(" ")}')#count tira os espaços das estrigs 
time.sleep(2)
print(f'seu primeiro nome tem {nome.find(" ")}')
#find conta quantas letras tem o primeiro nome