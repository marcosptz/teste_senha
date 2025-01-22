import time
from itertools import product

def teste1():
	caracteres = [0, 1, 2, 'a']
	permsList = [''.join(str(i) for i in x) for x 	in product(caracteres, repeat=2)]
	print(permsList)

def teste2():
	alfa1 = []
	#carac = [0, 1,  2, 3, 4, 5, 6, 7 , 8, 9]
	carac = [ 'e', 't', 's', 'T', '@', 0, 1,  2, 3, 4, 5, 6, 7 , 8, 9]
	aux = ''
	count = 0
	password = 'Test@7'
	#password = '193232'
	tempo_ini = time.time()
		
	for i in carac:
		for x in carac:
			for y in carac:
				for n in carac:
					for z in carac:
						for a in carac:
							count = count + 1
							aux = str(i) + str(x) + str(y) + str(n) + str(z) + str(a)
							#print(' ', aux)
							if(aux == password):
								tempo_fim = time.time()
								tempo = time.time() - tempo_ini
								print('_' * 30)
								print()
								print('Senha encontrada:', password)
								print('-' *30)
								print('Tempo denexecução:', round(tempo, 2), 's')
								#print('Tempo de execução:', round(tempo/0.60, 2) if tempo > 1 else round(tempo, 2), 's')
								print('Tentativas:', count)
								exit()

				
	print()
	print('-' * 30)
	print(' Tempo de execução:', round(time.time() - tempo_ini, 2),' s')				
	print(' Senha não encontrada!')
	print(' Tentativas:', count)
	
teste2()

#obj1 = [1,2,3]
#obj2 = [3,4,5,6]
#obj = obj1 + obj2
#print(obj)