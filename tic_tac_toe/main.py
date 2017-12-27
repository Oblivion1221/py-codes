import tictactoe as t

if __name__ == '__main__':
    print('Choose the game mode')
    inpt = input('Enter \'a\' for PvP, \'b\' for PvE: ')
    while True:
        if inpt == 'a':
            print('You are Player X, the other player is O')
            t.TicTacToe(mode=1)
            break
        elif inpt == 'b':
            print('You are Player X, the program is the other player O')
            t.TicTacToe(mode=2)
            break
        else:
            inpt = input('Please enter \'a\' or \'b\': ')
