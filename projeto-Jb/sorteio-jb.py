import random 
import time


bicho = ['1 Avestruz','2 Águia','3 Burro','4 Borboleta','5 Cachorro','6 Cabra',' 7 Carneiro','8 Camelo.','9 Cobra'
'10 Coelho','11 Cavalo ','12 Elefante','13 Galo','14 Gato','15 Jacaré','16 Leão ','17 Macaco','18 Porco ',
'19 Pavão ','20 Peru ','21 Touro','22 Tigre ','23 Urso','24 Veado ','25 Vaca'] 

grupo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 

bicho_dezena = ['Avestruz: 01, 02, 03, 04','Águia: 05, 06, 07, 08','Burro: 09, 10, 11, 12','Borboleta: 13, 14, 15, 16','Cachorro: 17, 18, 19, 20,','Cabra: 21, 22, 23, 24','Carneiro: 25, 26, 27, 28','Camelo: 29, 30, 31, 32','Cobra: 33, 34, 35, 36','Coelho: 37, 38, 39, 40','Cavalo: 41, 42, 43, 44','Elefante: 45, 46, 47, 48','Galo: 49, 50, 51, 52','Gato: 53, 54, 55, 56','Jacaré: 57, 58, 59, 60','Leão: 61, 62, 63, 64','Macaco: 65, 66, 67, 68','Porco: 69, 70, 71, 72','Pavão: 73, 74, 75, 76','Peru: 77, 78, 79, 80','Touro: 81, 82, 83, 84','Tigre: 85, 86, 87, 88','Urso: 89, 90, 91, 92','Veado: 93, 94, 95, 96','Vaca: 97, 98, 99, 00']


bicho = random.choice(bicho)
dezenas = random.choice(bicho_dezena) 

print('Analisando jogo do bicho >>>') 
time.sleep(5)
print(f"O bicho que vai da e;  bicho com dezena:({dezenas}) do grupo ({bicho}) << Bicho ")
