from easygui import passwordbox


jogador1 = passwordbox('Escolha: PEDRA (pe),PAPEL (pa) ou TESOURA (te)','JOGADOR 1')
jogador2 = passwordbox('Escolha: PEDRA (pe),PAPEL (pa) ou TESOURA (te)','JOGADOR 2 ')

if (jogador1 =='pe' and jogador2 == 'te') or (jogador1 == 'te' and jogador2 =='pa') or (jogador1 == 'pa' and jogador2 =='pe'):
    print('Jogador 1 venceu')
elif (jogador1 =='pe' and jogador2 == 'pe') or (jogador1 == 'pa' and jogador2 =='pa') or (jogador1 == 'te' and jogador2 =='te'):
    print('empatou')
else:
    print('jogador 2 venceu')
if (jogador1 =='pa' and jogador2 == 'te') or (jogador1 == 't' and jogador2 =='pa'):
    print('Tesoura corta  papel')
elif (jogador1 =='pe' and jogador2 == 'te') or (jogador1 == 't' and jogador2 =='pe'):
    print('Pedra quebra tesoura')
else:
    print('papel cobre pedra')
