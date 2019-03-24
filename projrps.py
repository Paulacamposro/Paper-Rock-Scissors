import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def play(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def play(self):
        random.randint(0, 2)


class HumanPlayer(Player):
    def play(self):
        player_move = input('Type Rock, Paper or Scissors!\n')
        while player_move not in moves:
            player_move = input('Type again!\n')
        return player_move


class ReflectPlayer(Player):
    def play(self):
        return self.their_move


class CyclePlayer(Player):
    def play(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        player1_score = 0
        player2_score = 0
        ties = 0

    def play_game(self):
        print("Buona fortuna!Game start!")
        for round in range(5):
            print(f'\n')
            print(f"Round {round}:")
            self.play_round()

        if self.player1.score > self.player2.score:
            print('\nBravo! Player 1 won!')
        elif self.player1.score < self.player2.score:
            print('\nAnche tu sei bravo! Player 2 won!')
        else:
            print('Come mai!The game was a draw!')
        print(f'\n Score : {self.player1.score} x {self.player2.score}')
        print("Game over!")

    def play_round(self):
        move1 = self.player1.play()
        move2 = self.player2.play()
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)
        print(f"Player 1: {move1}  Player 2: {move2}")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

    if move1 == move2:
        ties += 1
        print('\nDraw!')
    elif beats(move1, move):
        player1_score += 1
        print('\nPlayer 1 won!')
    else:
        player2_score += 1
        print('\nPlayer 2 won!')


if __name__ == '__main__':
    behaviors = random.randint(0, 2)
    if behaviors == 0:
        behaviors = RandomPlayer()
    elif behaviors == 1:
        behaviors = ReflectPlayer()
    else:
        behaviors = CyclePlayer()

human = HumanPlayer()
game = Game(human, behaviors)
game.play_game()
