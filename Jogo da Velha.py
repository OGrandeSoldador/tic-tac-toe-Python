# Função que imprime um matriz modificada com o estado atual do jogo.
def print_game(matriz):
    print('')
    for i in (0,3,6):
        print("   ",matriz[i],matriz[i + 1],matriz[i + 2])
    print('')


# Função que determina qual jogador atual.
def player_corrent(turn):
    if turn % 2 == 0:
        return 2
    else:
        return 1


# Função que solicita e valida a entrada de uma posição escolhida pelo usuário.
def get_position_played(player):
    print(f'Jogador {player}')
    get_position = int(input('Escolha uma posição: '))
    return get_position


# Função que guanda a jogado feita a cada rodada modificando a matriz.
def modify_game(position,player,matriz):
    if player == 1:
        x = 'X'
        matriz[position - 1] = x
        return matriz
    if player == 2:
        o = 'O'
        matriz[position - 1] = o
        return matriz


# Função que conferi possibilidade de vitória.
def win_condition(matriz):
    if matriz[0] == matriz[1] == matriz[2]:
        winner = matriz[1]
        return winner

    elif matriz[3] == matriz[4] == matriz[5]:
        winner = matriz[4]
        return winner

    elif matriz[6] == matriz[7] == matriz[8]:
        winner = matriz[7]
        return winner

    elif matriz[0] == matriz[3] == matriz[6]:
        winner = matriz[3]
        return winner

    elif matriz[1] == matriz[4] == matriz[7]:
        winner = matriz[4]
        return winner

    elif matriz[2] == matriz[5] == matriz[8]:
        winner = matriz[5]
        return winner

    elif matriz[0] == matriz[4] == matriz[8]:
        winner = matriz[4]
        return winner

    elif matriz[2] == matriz[4] == matriz[6]:
        winner = matriz[4]
        return winner

    else:
        return 1


# Função que conderi e informa quem foi o vencedor.
def who_is_the_winner(winner):
    print('\n')
    win = 'é o vencedor!'
    player1 = 'Jogador 1 '
    player2 = 'Jogador 2 '

    if winner == 'X':
        print(player1 + win)
    elif winner == 'O':
        print(player2 + win)


def main():

    matriz = ['1','2','3','4','5','6','7','8','9']
    t = 0
    print('Jogo da Velha')
    print_game(matriz)
    while t != 9:
        t += 1
        player = player_corrent(t)
        position = get_position_played(player)
        while matriz[position - 1] == 'X' or matriz[position - 1] == 'O':
            print('\nEscolha uma posição válida\n')
            position = get_position_played(player)
        modify_game(position,player,matriz)
        print_game(matriz)
        if win_condition(matriz) != 1:
            t = 9
            who_is_the_winner(win_condition(matriz))
        elif t == 9:
            print('Empate! ')
            print('\n''\n')


if __name__ == "__main__":
    main()
