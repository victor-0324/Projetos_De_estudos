print('\n======================================================================\nOi esse programa foi feio por vitor, ele serve para calcular\nquanto tera que paga no cartao de credito e calcula tanbém\nquanto ficara o total com juros padrao de 16%, aproveite\n======================================================================\n')
while True:
    try:
        cart = int(input('Quanto foi o gasto do més ?')) 
        paga = int(input(f"Ok, voce gastou  {cart}, quanto voce quer paga do cartáo ? ")) 
        restante = cart - paga 

        juros_atraso = restante * 16/100 

        total = juros_atraso + restante

        if paga < cart:
            print('\n======================================================================')
            print(f"\nVocé tera que paga uma taxa de juros de {juros_atraso}! se pagar {paga},\nficara restando do cartão {restante},\nsomando um valor total de {total}." )                        
            try:
                se_paga = str(input('Voce deseja paga com juros na proxima fatura ?'))   
                if se_paga.lower() == 'sim':
                    print('            ==========              ')
                    print(f'Ok, voce pagara um valor de {total}')
                    print('\n======================================================================\n')
                    juros  = str(input('A alguma fatura em aberto proximo mes?'))                   
                    if juros.lower() == 'sim':
                        print('            ==========              ')
                        juros2 = int(input('\ndigite o valor para somar '))
                        total2 = total + juros2 
                        print(f'================ Você pagara o valor total de {total2}! ================\n')
                        
                        break 
                    elif juros.lower() == 'nao':
                        print('            ==========              ')
                        print(f'Otimo voce pagara o valor total de {total}.')
                        print('volte sempre.\n')
                        break 
                    else:
                        print('\n======================================================================')
                        print('digite uma resposta valida!\n')
                elif se_paga.lower() == 'nao':
                    print('\n======================================================================')
                    print(f'Então voce deve paga o valor total do cartão que e {cart}!, e não pagagara juros \n')
                    break
                else:
                   
                    print('digite uma resposta valida S[im] ou N[ão]:\n')
            except:
                print('\n========================     Erro!    ================================')
                print('Algo deu errado verifique se esta informando as resposta corretamente\n ')
        elif paga == cart:
            print('            ==========             ')
            print('O seu pagamento foi efetivado com sucesso e não vai paga nenhum juros por atraso esse mes\ncontinui a sim !')

        else:
            print("digite um valor valido!\n") 

    except:
        print('\n========================     Erro!    ================================')
        print('Algo deu errado verifique se esta informando as resposta corretamente!\n ')