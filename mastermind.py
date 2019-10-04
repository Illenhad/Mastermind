from player import Player
from game import Game


def main():
    game_board = Game()
    game_board.game_title()

    player_one = Player(1)
    player_one.set_name()

    player_two = Player(2)
    player_two.set_name()

    game_board.game_difficulty()
    game_board.game_mod()

    game_board.game_title_resume(player_one.name, player_two.name)
    game_board.game_choice_color()

if __name__ == '__main__':
    main()
