from player import Player
from game import Game


def main():
    color_choice = ["R", "G", "R", "V", "R", "H"]
    color_result = ["R", "W", "W", "X", "X", "X"]
    color_choice_save = [color_choice, color_choice, color_choice]
    color_result_save = [color_result, color_result, color_result]

    game_board = Game()
    game_board.game_title()

    player_one = Player(1)
    player_one.set_name()

    player_two = Player(2)
    player_two.set_name()

    game_board.game_difficulty()
    game_board.game_mod()

    game_board.game_title_resume(player_one.name, player_two.name)

    game_board.game_board_view(color_choice_save, color_result_save)

if __name__ == '__main__':
    main()
