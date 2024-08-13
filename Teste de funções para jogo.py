matriz = ['0','1','2','3','4','5','6','7','8']


# Função que guanda a jogado feita a cada rodada modificando a matriz.
def modify_list(position,player):
    if player == 1:
        x = 'X'
        matriz[position - 1] = x
        return matriz
    if player == 2:
        o = 'O'
        matriz[position - 1] = o
        return matriz

# Função que determina qual jogador atual.
def player_corrent(turn):
    if turn // 2 == 0:
        return 2
    else:
        return 1

# Função que solicita e valida a entrada de uma posição escolhida pelo usuário.
def get_position_played(turn):
    get_position = int(input('Escolha uma posição: '))
    return get_position


def main():

    get_position_played(1)
    # modify_list(input_position,player)
    # print(modify_list(input_position,p
    # print(modify_list(3,1))



if __name__ == "__main__":
    main()
