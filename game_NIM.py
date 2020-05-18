def computador_escolhe_jogada( n, m):
    computadorRemove=1

    while computadorRemove!=m:
        if (n-computadorRemove) % (m+1)==0:
            return computadorRemove
        else:
            computadorRemove+=1

    return computadorRemove


def usuario_escolhe_jogada( n, m):
    jogadaValida=False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove>m or jogadorRemove<1:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogadaValida=True

    return jogadorRemove


def campeonato():
    numeroRodada=1
    while numeroRodada<=3:
        print('\n**** Rodada', numeroRodada, '****\n')
        partida()
        numeroRodada+=1
    print('\nPlacar: Você 0 X 3 Computador\n')


def partida():
    n=int(input('Quantas peças? '))
    m=int(input('Limite de peças por jogada? '))

    MAQUINA = False

    if n%(m+1)==0:
        print('\nVoce começa!\n')

    else:
        print('\nComputador começa!\n')
        MAQUINA=True

    while n>0:
        if MAQUINA:
            computadorRemove=computador_escolhe_jogada( n, m)
            n=n-computadorRemove
            
            print(computadorRemove==1 and 'O computador tirou uma peça\n' or 'O computador tirou', computadorRemove, 'peças\n')

            MAQUINA=False
        else:
            jogadorRemove=usuario_escolhe_jogada( n, m)
            n=n-jogadorRemove
            
            print(jogadorRemove==1 and 'Você tirou uma peça\n' or 'Você tirou', jogadorRemove, 'peças\n')

            MAQUINA=True
        if n==1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n!=0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')
               

    print('Fim do jogo! O computador ganhou!')

def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato ')

    opcao=int(input('Escolha: '))

    if opcao==2:
        print('\nVoce escolheu um campeonato!\n')
        campeonato()
    else:
        if opcao==1:
            partida()

main()
