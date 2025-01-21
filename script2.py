import time
import string

def testeSenha():
	#val = string.ascii_letters
	val = string.ascii_uppercase + '@#'
	val += string.ascii_lowercase
	val += string.digits
	tempo_ini = time.time()
	senha = 'ABCDEF'
	aux = ''

	for i in val:
		for x in val:
			for y in val:
				for n in val:
					for p in val:
						for r in val:
							#for s in val:
							aux = i + x + y + n + p + r
							#print(' ', aux)
							if (aux == senha):
								print(' Senha encontrada:', aux)
								tempo = time.time() - 		tempo_ini
								print(' Tempo:', tempo)
								exit()
							
	print('Senha não encontrada!')	
	tempo = time.time() - tempo_ini
	print(' Tempo:', tempo)
			
testeSenha()