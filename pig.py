import random
import argparse

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0

    def roll(self, die):
        roll = die.roll()
        if roll == 1:
            self.turn_total = 0
            return roll
        else:
            self.turn_total += roll
            return roll

    def hold(self):
        self.score += self.turn_total
        self.turn_total = 0


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Game:
    def __init__(self, playerone, playertwo):
        self.players = [playerone, playertwo]
        self.die = Die()
        self.current_player = self.players[0]

    def start(self):
        while not self.is_game_over():
            print("It's", self.current_player.name + "'s turn.")
            print("Current score:", self.current_player.score)
            print("Turn total:", self.current_player.turn_total)
            decision = input("Enter 'r' to roll or 'h' to hold: ")
            if decision == 'r':
                roll = self.current_player.roll(self.die)
                print("You rolled a", roll)
                if roll == 1:
                    print("Turn over.")
                    self.switch_players()
            elif decision == 'h':
                self.current_player.hold()
                print("Turn over.")
                self.switch_players()
            else:
                print("Invalid input. Try again.")

    def switch_players(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def is_game_over(self):
        for player in self.players:
            if player.score >= 100:
                print(player.name, "wins!")
                return True
        return False

    def reset(self):
        for player in self.players:
            player.score = 0
            player.turn_total = 0
        self.current_player = self.players[0]


if __name__ == '__main__':
    playerone = Player("Player 1")
    playertwo = Player("Player 2")
    game = Game(playerone, playertwo)
    game.start()
