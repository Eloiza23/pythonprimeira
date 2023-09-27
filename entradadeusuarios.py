# declarar variavel que vai receber
# a entrada pelo teclado

#entrada
aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2:'))

#processamento
media = (n1+ n2)/2

#saida
print('Nome do aluno:', aluno.lower())#letras
print('Nome do aluno:', aluno.upper())
print('Nome do aluno:', aluno.title())


print('Nota 1:', n1)
print('Nota 2:', n2)
print('sua média final foi:',media)