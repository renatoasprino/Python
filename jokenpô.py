

jogador1 =input('Escolha: PEDRA (p),PAPEL (pa) ou TESOURA (t)',)
jogador2 = input(' JOGADOR 2-Escolha: PEDRA (p),PAPEL (pa) ou TESOURA (t) ')

if (jogador1 =='p' and jogador2 == 't') or (jogador1 == 't' and jogador2 =='pa') or (jogador1 == 'pa' and jogador2 =='p'):
    print('Jogador 1 venceu')
elif (jogador1 =='p' and jogador2 == 'p') or (jogador1 == 'pa' and jogador2 =='pa') or (jogador1 == 't' and jogador2 =='t'):
    print('empatou')
else:
    print('jogador 2 venceu')
if (jogador1 =='pa' and jogador2 == 't') or (jogador1 == 't' and jogador2 =='pa'):
    print('Tesoura corta  papel')
elif (jogador1 =='p' and jogador2 == 't') or (jogador1 == 't' and jogador2 =='p'):
    print('Pedra quebra tesoura')
else:
    print('papel cobre pedra')
    