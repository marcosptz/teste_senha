# Script que recupera senhas
import sys
import string
import time
import pikepdf
from odf import text, teletype
from odf.opendocument import load
from datetime import timedelta
from itertools import permutations
from itertools import combinations_with_replacement
# from itertools import nth_combination_with_replacement
from random import random, choice

def main(args):
    valores = string.ascii_letters
    valores += string.digits
    valores += '@#$,.'
    # valores += string.punctuation
    tamanho = 4

    # print('valores', valores)

    temp_ini = time.time()
    gerar_senha(valores, tamanho)
    temp_fin = time.time()

    print('Tempo: ' + str(temp_fin - temp_ini) + 's')

def gerar_senha(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho)
    pwd = '12345'
    # comb = permutations(valores, tamanho)

    # print("Qtd combinacoes:" + str(len(list(comb))))
    print(', '.join(list(comb)[0]))

    textdoc = load("teste_senha.odt", pasword="12345")
    print(textdoc)
    # try:
    #     with open('teste_senha.pdf', 'r') as arquivo:
    #         conteudo = arquivo.read()
    #         print(conteudo)
    #     exit()
    # except:
    #     print('Erro')


# valores = 'abc'
# gerar_senha(valores, 3)

# txt = ["".join(_) for _ in permutations('12345')]

# print(txt)
  
# a ="GEeks"
 
# l = list(combinations_with_replacement(a, 2))
# print("COMBINATIONS WITH REPLACEMENTS OF STRING GEeks OF SIZE 2.")
# print(l)

if __name__ == '__main__':
    main(sys.argv[1:])
    # gerar_senha('abc', 3)
