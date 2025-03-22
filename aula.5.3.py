with open('exemplo.txt' , 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('exemplo.txt', 'r') as arquivo:
    linha1 = arquivo.readline()
    print(linha1)
    linha1= arquivo.readline()
    print(linha1)

with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)