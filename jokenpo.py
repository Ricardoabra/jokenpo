print('-------------------')
print()
print('      JOKENPO      ')
print()
print('-------------------')
print()
print('Escolha uma das opções:')
print()
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
print('-------------------')
print()
n = int(input('Digite sua opção:'))
print('-------------------')

if n == 1:
    print('Você escolheu PEDRA.')
elif n == 2:
    print('Você escolheu PAPEL.')
elif n == 3:
    print('Você escolheu TESOURA.')
else:
    print('Escolha uma das opções válidas.')

print()
import random
numero = random.randint(1, 3)  
if numero == 1:
    print('A máquina escolheu PEDRA.')
elif numero == 2:
    print('A máquina escolheu PAPEL.')
elif numero == 3:
    print('A máquina TESOURA.')
print('-------------------')
print()
if n==1 and numero == 1:
    print('EMPATE!')
elif n == 1 and numero == 2:
    print('A MÁQUINA GANHOU!')
elif n == 1 and numero == 3:
    print('VOCÊ GANHOU!')
elif n == 2 and numero == 1:
    print('VOCÊ GANHOU!')
elif n == 2 and numero == 2:
    print('EMPATE!')
elif n == 2 and numero== 3:
    print('A MÁQUINA GANHOU!')
elif n == 3 and numero == 1:
    print('A MÁQUINA GANHOU!')
elif n == 3 and numero == 2:
    print('VOCÊ GANHOU!')
elif n == 3 and numero == 3:
    print('EMPATE!')