import time 


nome = str(input('qual e seu nome ? ')) 
idade = int(input(f'Ok {nome}, quantos anos voçe tem ?  ')) 
if idade > 18:
    print('voçe e de maior, pode tentar o enprestimo \n ') 
    print('para o senhor ser a provado no enprestimo \n voçe nao pode outrapassa 30% do seu salario ok \n ')
    b = float(input(f'quanto e a casa R$ {nome} ?'))
    valor_casa = b

    a = float(input('Quanto e o seu salario R$ ? '))
    salario = a 

    c = int(input('em quantos anos voçe que pagar R$ ?')) 
    anos_apaga = c  

    valor = valor_casa / (anos_apaga * 12)
    minimo = salario - salario * 30/100
    print('ok vamos analizar seu pedido... ')
    time.sleep(2) 
    
    print(F'para pega a casa de {valor_casa} em {anos_apaga} anos ' ,end= ('')) 
    print(f'A prestaçao sera de {valor} ') 
    if valor <= minimo:
        print('Enprestimo pode ser CONCEDIDO!!') 

    else:
        print('Enprestimo nao pode ser CONCEDIDO!')
    
elif idade < 18:
    print('voçe e de menor e nao pode fazer o enprestimo')
