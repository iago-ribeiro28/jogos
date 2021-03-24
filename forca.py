import random


def jogar_forca():
    mensangem_inicial()
    palavra_secreta = selecionar_palavras()
    letra_acertada = letras_acertadas(palavra_secreta)
    print(letra_acertada)

    enforcou = False
    acertou = False
    erros = 0
    acertos = 0

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letra_acertada, acertos)
        else:
            erros += 1
            desenha_forca(erros)

        print(letra_acertada)
        acertou = '_' not in letra_acertada
        enforcou = erros == 7

        vencedor_perdedor(acertou, enforcou, palavra_secreta)


def mensangem_inicial():
    print('*' * 33)
    print('***Bem vindo ao jogo da forca!***'.upper())
    print('*' * 33)


def selecionar_palavras():
    arquivos = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivos:
        linha = linha.strip()
        palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def letras_acertadas(palavra):
    return ['_' for _ in palavra]


def pede_chute():
    chute = input('Qual letra? ').upper().strip()
    return chute


def marca_chute_correto(palavra_secreta, chute, letra_acertada, acertos):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            letra_acertada[index] = letra
            acertos += 1
        index += 1


def desenha_forca(erros):
    print(f'Você errou, restam {7 - erros} tentativas.')

    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3 :
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def vencedor_perdedor(acertou, enforcou, palavra_secreta):
    if enforcou:
        print('Game Over!')
        print("Puxa, você foi enforcado!")
        print(f'A palavra era {palavra_secreta}')
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print('       \_______/           ')
    elif acertou:
        print('\n\033[4;7mVocê venceu!! Parabéns!!\033[m')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


if __name__ == '__main__':
    jogar_forca()