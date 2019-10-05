from player import Player
from game import Game


def main():
    color_result = ["O", "O", "X", "", "", ""]

    game_board = Game()
    # game_board.game_title()

    # player_one = Player(1)
    # player_one.set_name()

    player_two = Player(2)
    # player_two.set_name()
    #
    game_board.game_difficulty()
    # game_board.set_mod()
    #
    # game_board.game_title_resume(player_one.name, player_two.name)

    x = 0
    while x < 4:
        game_board.game_board_view()
        game_board.color_choice_save.append(player_two.select_colors(game_board.color_list))
        game_board.color_result_save.append(color_result)
        x = x + 1

    input("Press Enter to continue...")


if __name__ == '__main__':
    main()
