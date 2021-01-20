#simula o uso de um dado, gerando um valor de 1 ate 6 
import random
import PySimpleGUI as sg 

class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6 
        self.mensagem = 'Voçe gostaria de gera um novo valor para o dado ? '
        #layout
        self.layout = [ 
            [sg.Text('Jogar o dado ? ')],
            [sg.Button('sim'),sg.Button('nao')]
            
        ] 
       

    def iniciar(self):
         #cria uma janela 
        self.janela = sg.Window('simulador de dados',layout=self.layout)
        #ler os valores de tela 
        self.eventos,self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores        
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                #print('Agradecemos a sua partipaçao')
                self.gerarvalordodado() 
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('Agradecemos a sua partipaçao')
            else:
                print('digete sim ou nao')                        
        except:
            print('O correu um erro au receber sua resposta')
            
    def gerarvalordodado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo)) 

simulador = SimuladorDeDados()
simulador.iniciar()       



   