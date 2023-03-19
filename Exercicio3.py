#Exercicio3
#Crie um programa em Python que solicite um número do usuário, depois some este número com 1357,
# multiplique por 8, divida por 5 e eleve ao quadrado.


numero=int (input('Digite um numero entre 1 e 9 para criar o seu usuario: '))
numero2=1357
t=int((((numero+numero2)*8)/5)**2)
print(f'seu usuario é {t}')