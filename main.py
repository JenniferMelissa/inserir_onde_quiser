#lista de nomes
nomes = ['Filano','Cicrano','Beltrano']

#usuario insere novo nome
novo_nome = input('Informe o novo nome: ').capitalize()
posicao = int(input('Informe a posição do novo item: '))
#captalize colica a primeira letra como maiuscula

#insere o novo nome no local indicado
nomes.insert(posicao,novo_nome)
#


#imprime a lista
for nome in nomes:
    print(nome)

#ordena lista
nomes.sort()

print('\n')

#imprime a lista nova
for nome in nomes:
    print(nome)

