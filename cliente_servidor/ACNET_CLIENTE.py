print('Ola nos da empresa AcNet estamos fazendo uma pesquisa\n para saber como esta nosso serviço de  internet na sua casa\n ')
primeiro = input('Como e o seu nome ?'.strip())
a = primeiro
segundo = input(f'Qual bairro voçe mora {a} ?\n '.strip())
b = segundo
terceiro = int(input(f'muito bem de uma escala de 0 a 10 {a} \n quanto o senhor(a) e satisfeito com nosso serviço de internet \n No bairro {b} ?\n '))
c = terceiro 
if c <= 5:
  print(f'Obrigado {a} pelo seu fedback,\n ')
  print(f'Vamos começa a melhorar nossos serviços no bairro {b}\n para melhor atender voçe cliente') 
  pergunta = int(input('Qual problema o senhor tem ?\n 1= lentidao \n 2= sem internet durante certa hora do dia \n responda 1 ou 2\n '))
  c = pergunta
  if c == 1:
    print(f'vamos começa uma varredura na rede do bairro {b} \n para averiguar posiveis problemas de rede, a ACNET a gradece sua preferencia OBRIGADO !!') 
  elif c == 2:
    print(f'Vamos enviar um tecnico ate sua residencia senhor(a) {a}\n para a veriguar posiveis problemas em seu modem a ACNET a gradece sua preferencia OBRIGADO!!\n ')  
  else:
    print('Digete uma das opçao sitada a cima obrigado ')
elif c > 5 and c < 11:
  print(f'obrigado {a} pela sua nota >> {c}\n nos taremos sempre melhorando nosso serviços no bairro {b}\n ') 
else:
  print(f'digete um numero de (0 a 10) por favor {a}\n')   
print(f'nome do cliente >({a})<') 
print(f'nome do bairro do cliente > ({b}) <') 
print(f'nota do cliente foi >({terceiro})<') 
if terceiro <= 5:
  print(f'cliente insatisfeito no bairro {b} ') 
else:
  print(f'o cliente esta satisfeito a nota foi >> {terceiro} << ')