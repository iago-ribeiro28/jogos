import random


def jogar_par_ou_impar():

    mensagem_inicial()

    comp = random.randint(1, 2)

    contador = 0
    vencendo = False

    while not vencendo:

        escolha = escolha_par_impar()

        numero = int(input('Coloque o número que deseja jogar: '))

        print(f'O computador jogou {comp}')

        perdeu = derrota(comp, escolha, numero)

        if perdeu:
            break
        else:
            contador += 1
            print('Você venceu!')
            comp = random.randint(1, 2)

    mensagem(contador)


def mensagem_inicial():
    print('*' * 23)
    print('***Jogo Par ou Impar***')
    print('*' * 23)


def escolha_par_impar():
    escolha = 'N'
    while escolha != 'P' and escolha != 'I':
        escolha = input('Par ou ímpar? [P/I] ').strip().upper()
    return escolha


def derrota(comp, escolha, numero):
    derrota1 = escolha == 'P' and (numero + comp) % 2 == 1
    derrota2 = escolha == 'I' and (numero + comp) % 2 == 0
    perdeu = derrota1 or derrota2
    return perdeu


def mensagem(contador):
    print(f"""Você perdeu, boa sorte na próxima!
    Você venceu {contador} partidas.""")


if __name__ == '__main__':
    jogar_par_ou_impar()
