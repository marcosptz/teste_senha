import time
import string
from itertools import product

def testeSenha():
	#val = string.ascii_letters
	# val = string.ascii_uppercase + '@#'
	# val += string.ascii_lowercase
	val = string.digits
	tempo_ini = time.time()
	senha = '112456789'
	aux = ''
	count = 0

	for i in val:  # 1 dígito
		for x in val:  # 2 dígito
			for y in val:  # 3 dígito
				for n in val:  # 4 dígito
					for p in val:  # 5 dígito
						for r in val:  # 6 dígito
							for s in val:  # 7 dígito
								for u in val:  # 8 dígito
									for v in val:  # 9 dígito
										# for z in val:  # 10 dígito
										count = count + 1
										aux = i + x + y + n + p + r + s + u + v
										#print(' ', aux)
										if (aux == senha):
											print('Senha encontrada:', aux)
											tempo = time.time() - tempo_ini
											print('Tempo:', tempo)
											print('Tentativas:', count)
											exit()
							
	print('Senha não encontrada!')	
	tempo = time.time() - tempo_ini
	print(' Tempo:', tempo)


def testeSenha2():
	# caracteres = [0, 1, 2, 'a']
	caracteres = string.ascii_uppercase + '@#'
	caracteres += string.ascii_lowercase
	caracteres += string.digits
	tempo_ini = time.time()
	senha = '123456789'
	aux = ''
	count = 0
	# ''.join(str(i) for i in x):
	# for x in product(caracteres, repeat=2):
	# 	print(x)

	permsList = [''.join(str(i) for i in x) for x in product(caracteres, repeat=6)]
	# print(permsList)
	tempo = time.time() - tempo_ini
	print(' Tempo:', tempo)	



testeSenha()