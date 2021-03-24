from random import randint


def jogar_adivinhacao():

    mensagem_inicial()

    numero_do_jogador = estabelecer_numero_jogador()
    numero_do_computador = estabelecer_numero_computador()

    derrota = False
    contador = 0

    while not derrota:

        derrota = verificacao_de_numeros(numero_do_jogador, numero_do_computador)

        if not derrota:
            print('Você venceu!')
            numero_do_jogador = estabelecer_numero_jogador()
            numero_do_computador = estabelecer_numero_computador()
            contador += 1
        else:
            print(f'Você perdeu!!\n'
                  f'O número era: {numero_do_computador}')

    mensagem_final(contador)


def mensagem_inicial():
    print('*' * 38)
    print('***Bem vindo ao jogo da Advinhação!***'.upper())
    print('*' * 38)

    print('Coloque um número entre 1 até 5.\n'
          'Se esse número for igual ao do computador'
          ' você vence a rodada. Boa sorte!!\n')


def estabelecer_numero_jogador():
    numero_do_jogador = int(input('Digite o número entre 1 até 5: '))
    return numero_do_jogador


def estabelecer_numero_computador():
    numero_do_computador = randint(1, 5)
    return numero_do_computador


def verificacao_de_numeros(numero_do_jogador, numero_do_computador):
    derrota = True
    if numero_do_jogador == numero_do_computador:
        derrota = False
    return derrota


def mensagem_final(contador):
    if contador == 1:
        print(f'Obrigado por jogar!\n'
              f'Você venceu {contador} rodada')
    elif contador > 1:
        print(f'Obrigado por jogar!\n'
              f'Você venceu {contador} rodada')
    else:
        print('Obrigado por jogar!\n'
              'Mais sorte na próxima tentativa')


if __name__ == '__main__':
    jogar_adivinhacao()
