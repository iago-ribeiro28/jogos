import forca
import Par_ou_impar
import Adivinhacao


jogando = 'S'

while jogando == 'S':

    print('*'*22)
    print('***Escolha seu jogo***')
    print('*'*22)

    print("""
(1) Advinhação
(2) Forca
(3) Par ou impar""")

    jogo = 0

    while 3 < jogo < 1:

        jogo = int(input('\nQual jogo? '))

        if jogo == 1:
            Adivinhacao.jogar_adivinhacao()
        elif jogo == 2:
            forca.jogar_forca()
        else:
            Par_ou_impar.jogar_par_ou_impar()

    jogando = input('Gostaria de jogar outro jogo? [S/N]').strip().upper()

print('Obrigado por jogar')
