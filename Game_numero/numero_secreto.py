import random

def jogo_numero_secreto():
    print(" ")
    print("#############################################")
    print("Bem vindo ao jogo do Numero Secreto em Python!")
    print("#############################################")
    print(" ")

    #Escolhendo o intervado de numeros exemplo de 01 ate 100
    numero_maximo = int(input('Escolha o numero maximo: '))
    numero_secreto = random.randrange(1, numero_maximo)
    print(numero_secreto)
    tentativas = 0
    pontos_acumulado = 1000

    #Que tal escolher a dificuldade do jogo ? ;)
    print("Qual a dificuldade ?")
    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input())


    #Validação da dificuldade de jogo 
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    else:
        if(nivel > 3):
            print("Favor escolher essas dificuldade [(1) Facil (2) Medio (3) Dificil]")
        

    #Validando chute com o numero secreto
    for rodadas in range (1, tentativas + 1):
        print(f'Tentativas {rodadas} de {tentativas}')
        chute = int (input(f'Digite um numero entre 1 e {numero_maximo}: '))

        if (chute < 1 or chute > 100):
            print("#################################")
            print(f"Voce deve digitar um numero entre 1 e {numero_maximo}!")
            print("#################################")
            continue #retomar o inicio do laço
    
        acerto = numero_secreto == chute
        menor = numero_secreto < chute
        maior = numero_secreto > chute

        if(acerto):
            print(f'Parabens Voce acertou e fez: {pontos_acumulado}')
            break #Finalizando a função apos acerto, caso contrario continue 
        else:
            if(menor):
                print('Voce errou, o numero secreto e menor.')
            elif(maior):
                print('Voce errou, o numero secreto e maior')
            perdas = abs(numero_secreto - chute)
            pontos_acumulado = pontos_acumulado - perdas
    print('End Game')

if(__name__ == '__main__'):
    jogo_numero_secreto()