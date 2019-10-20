from player_class import Player
from game_class import Game


def main():
    game_board = Game()
    game_board.game_title()

    player_one = Player(1)
    player_one.set_name()

    player_two = Player(2)
    player_two.set_name()

    game_board.set_players(player_one,
                           player_two)

    game_board.game_difficulty()
    game_board.set_mod()

    game_board.game_title_resume(game_board.players[0].name,
                                 game_board.players[1].name)

    while game_board.game_continue:

        game_board.view_color()
        game_board.solution = game_board.players[0].select_colors(game_board.color_list)

        while game_board.game_continue:

            game_board.game_board_view()
            game_board.color_choice_save.append(
                game_board.players[1].select_colors(game_board.color_list)
            )
            game_board.verify_choice()
            game_board.verify_end_game()

        game_board.result_game()
        game_board.set_another_game()


if __name__ == '__main__':
    main()
