matriz = ['O','O','O',3,4,5,6,7,8]

'''def change_select_position(position,matriz):
     matriz_modified[] = matriz[position]
    return '''


def win_condition(modified):
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


def print_matriz(positions):
    for i in (0,3,6):
        print(matriz[i],matriz[i + 1],matriz[i + 2])
    print('\n')


def whoisthewinner(result):
    win = 'é o vencedor'
    player1 = 'Jogador 1 '
    player2 = 'Jogador 2 '

    if result == 'X':
        return print(player1 + win)
    elif result == 'O':
        return print(player2 + win)


def main():
    #position_select(2,matriz)
    whoisthewinner(win_condition(matriz))


if __name__ == "__main__":
    main()
