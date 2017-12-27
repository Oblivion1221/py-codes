import robot


class TicTacToe:
    CONST = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, mode):
        times = 1
        # 1st type of idiom expression to print the tictactoe board
        [print(c, end=" ") if (self.CONST.index(c) + 1) % 3 else print(c, '\n') for c in self.CONST]
        while True:
            if times % 2:
                try:
                    self.process(player='X')
                    if self.check_winner():
                        print('X wins!')
                        break
                    elif self.check_draw():
                        print('Nobody wins.. Try again.')
                        break
                except IndexError:
                    print("Your input is out of range. Please enter integers from 1 to 9.")
            else:
                if mode == 1:
                    try:
                        self.process(player='O')
                        if self.check_winner():
                            print('O wins!')
                            break
                        elif self.check_draw():
                            print('Nobody wins.. Try again.')
                            break
                    except IndexError:
                        print('Your input is out of range. Please enter integers from 1 to 9.')
                elif mode == 2:
                    pos = robot.easy_level(self.CONST)
                    self.CONST[pos - 1] = 'O'
                    print('The program\'s turn: ')
                    # 2nd type of idiom expression to print the tictactoe board
                    [print(self.CONST[i], end=" ") if (i + 1) % 3 else print(self.CONST[i], '\n') for i in
                     range(len(self.CONST))]
                    if self.check_winner():
                        print('Program wins!')
                        break
                    elif self.check_draw():
                        print('Nobody wins.. Try again.')
                        break
            times += 1

    def process(self, player):
        # global pos
        while True:
            try:
                pos = int(input("Which square, player {}? ".format(player)))
                break
            except ValueError:
                print("Enter your number again.")
        while self.CONST[pos - 1] and type(self.CONST[pos - 1]) is str:
            print("Sorry, that {} already took that square.".format(self.CONST[pos - 1]))
            [print(self.CONST[i], end=" ") if (i + 1) % 3 else print(self.CONST[i], '\n') for i in
             range(len(self.CONST))]
            pos = int(input("Which square, player {}? ".format(player)))
        self.CONST[pos - 1] = player
        [print(self.CONST[i], end=" ") if (i + 1) % 3 else print(self.CONST[i], '\n') for i in range(len(self.CONST))]

    def check_winner(self):
        return (self.CONST[0] == self.CONST[1] == self.CONST[2]) or \
               (self.CONST[3] == self.CONST[4] == self.CONST[5]) or \
               (self.CONST[6] == self.CONST[7] == self.CONST[8]) or \
               (self.CONST[0] == self.CONST[3] == self.CONST[6]) or \
               (self.CONST[1] == self.CONST[4] == self.CONST[7]) or \
               (self.CONST[2] == self.CONST[5] == self.CONST[8]) or \
               (self.CONST[0] == self.CONST[4] == self.CONST[8]) or \
               (self.CONST[2] == self.CONST[4] == self.CONST[6])

    def check_draw(self):
        draw = 0
        for c in self.CONST:
            if type(c) is int:
                draw = 0
                break
            elif type(c) is str:
                draw = 1
            else:
                continue
        return draw
