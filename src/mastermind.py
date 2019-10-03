from player import Player
from game import Game


def main():
    gameBoard = Game()
    gameBoard.gameTitle()

    player_one = Player(1)
    player_one.set_name()

    player_one = Player(2)
    player_one.set_name()

    gameBoard.gameDifficulty()


if __name__ == '__main__':
    main()
