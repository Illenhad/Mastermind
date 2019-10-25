from player_class import Player
from game_class import Game
from os import name as os_name


class TestGame:

    def test_game_init(self):
        """test Game.__init__"""
        game_board = Game()

        assert game_board.color_list == ['Yellow', 'Pink', 'Red', 'Aqua', 'White', 'Black', 'Orange', 'Violet']
        assert game_board.solution == []
        assert game_board.players == []
        assert game_board.difficulty_list == {1: "Normal", 2: "Difficult"}
        assert game_board.difficulty == 1
        assert game_board.mod_list == {1: "Normal", 2: "Debug"}
        assert game_board.mod == 1
        assert game_board.color_choice_save == []
        assert game_board.color_result_save == []
        assert game_board.game_continue
        assert game_board.another_game
        if os_name == 'posix':
            assert game_board.var_os == 'clear'
        else:
            assert game_board.var_os == 'cls'

    def test_set_players(self):
        """test Game.set_players"""
        game_board = Game()

        game_board.set_players('Pierre', 'William')
        assert game_board.players == ['Pierre', 'William']

    def test_verify_choice_1(self):
        """test Game.verify_choice with X: 4, O: 0"""
        game_board = Game()
        game_board.color_choice_save = [[1, 2, 3, 4]]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_choice()
        assert game_board.color_result_save == [{"X": 4, "O": 0}]

    def test_verify_choice_2(self):
        """test Game.verify_choice with X: 0, O: 4"""
        game_board = Game()
        game_board.color_choice_save = [[4, 3, 2, 1]]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_choice()
        assert game_board.color_result_save == [{"X": 0, "O": 4}]

    def test_verify_choice_3(self):
        """test Game.verify_choice with X: 2, O: 2"""
        game_board = Game()
        game_board.color_choice_save = [[1, 2, 4, 3]]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_choice()
        assert game_board.color_result_save == [{"X": 2, "O": 2}]

    def test_verify_choice_4(self):
        """test Game.verify_choice with X: 0, O: 0"""
        game_board = Game()
        game_board.color_choice_save = [[5, 6, 7, 0]]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_choice()
        assert game_board.color_result_save == [{"X": 0, "O": 0}]

    def test_verify_choice(self):
        """test Game.verify_choice with X: 1, O: 3"""
        game_board = Game()
        game_board.color_choice_save = [[1, 3, 4, 2]]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_choice()
        assert game_board.color_result_save == [{"X": 1, "O": 3}]

    def test_verify_end_game_1(self):
        """test Game.verify_end_game = 10 turn"""
        game_board = Game()
        game_board.color_result_save = [{"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0}]

        game_board.verify_end_game()

        assert game_board.game_continue == False

    def test_verify_end_game_2(self):
        """test Game.verify_end_game > 10 turn"""
        game_board = Game()
        game_board.color_result_save = [{"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0},
                                        {"X": 0, "O": 0}]

        game_board.verify_end_game()

        assert game_board.game_continue == False

    def test_verify_end_game_3(self):
        """test Game.verify_end_game < 10 turn and Win """
        game_board = Game()
        game_board.color_result_save = [{"X": 4, "O": 0}]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_end_game()

        assert game_board.game_continue == False

    def test_verify_end_game_4(self):
        """test Game.verify_end_game < 10 turn and don't Win """
        game_board = Game()
        game_board.color_result_save = [{"X": 0, "O": 0}]
        game_board.solution = [1, 2, 3, 4]

        game_board.verify_end_game()

        assert game_board.game_continue == True