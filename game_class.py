from os import name as os_name, system as os_system
import sqlite3


class Game:
    def __init__(self):
        self.color_list = ['Yellow', 'Pink', 'Red', 'Aqua', 'White', 'Black', 'Orange', 'Violet']
        self.solution = []
        self.players = []
        self.difficulty_list = {1: "Normal", 2: "Difficult"}
        self.difficulty = 1
        self.mod_list = {1: "Normal", 2: "Debug"}
        self.mod = 1
        self.color_choice_save = []
        self.color_result_save = []
        self.game_continue = True
        self.another_game = True

        # Verify OS to clear shell
        if os_name == 'posix':
            self.var_os = 'clear'
        else:
            self.var_os = 'cls'

    def game_title(self):

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("Welcome to Mastermind !"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" For a better experience, we recommend you"))
        print(" ║{:51}║".format(" to run this program in a real terminal,"))
        print(" ║{:51}║".format(" not in a python interpreter."))
        print(" ╚" + "═" * 51 + "╝")
        input("  Press Enter to continue...")

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("Player Name"))
        print(" ╚" + "═" * 51 + "╝")

    def set_players(self, p1, p2):
        self.players.append(p1)
        self.players.append(p2)

    def game_rules(self):

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("Game rules"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" Player One choose a combination of color"))
        print(" ║{:51}║".format(" Player Two must find out in less than 10 moves"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" In response of Player Two proposition :"))
        print(" ║{:51}║".format(" X for good color and good place"))
        print(" ║{:51}║".format(" O for good color and bad place"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" Two difficulty are available :"))
        print(" ║{:51}║".format(" In Normal, you can choose from 8 colors, "))
        print(" ║{:51}║".format(" and the combination contains 4 colors"))
        print(" ║{:51}║".format(" In Difficult, you can choose from 10 colors, "))
        print(" ║{:51}║".format(" and the combination contains 6 colors"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" Two mod are available."))
        print(" ║{:51}║".format(" In Normal mod, the solution is hidden"))
        print(" ║{:51}║".format(" In Debug mod, the solution is visible"))
        print(" ╚" + "═" * 51 + "╝")

        input("  Press Enter to continue...")

    """
    Set self.difficulty
    Difficult : add two colors into color list
    """
    def set_difficulty(self):
        res = ""

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")

        for difficulty in self.difficulty_list:
            res = res + "{:^} : {:^}  ".format(difficulty,
                                               self.difficulty_list[difficulty])

        print(" ║{:^51}║".format(res))
        print(" ╚" + "═" * 51 + "╝")

        while True:
            difficulty_choice = input("  Choose your difficulty : ")

            if len(difficulty_choice) == 1:
                if int(ord(difficulty_choice)) in (49, 50):
                    break

            print("  Enter the number before difficulty.")

        self.difficulty = int(difficulty_choice)

        if self.difficulty == 2:
            self.color_list.append('Gold')
            self.color_list.append('Silver')

        self.color_list.sort()

        print()

    """
    Set self.mod
    Normal : Solution is hidden
    Debug : Solution is visible 
    """
    def set_mod(self):
        res = ""

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")

        for mod in self.mod_list:
            res = res + "{:^} : {:^}  ".format(mod,
                                               self.mod_list[mod])

        print(" ║{:^51}║".format(res))
        print(" ╚" + "═" * 51 + "╝")

        while True:
            mod_choice = input("  Choose your mod : ")

            if len(mod_choice) > 0:
                if int(ord(mod_choice)) in (49, 50):
                    break

            print("  Enter 1 for Normal or 2 for Debug.")

        self.mod = int(mod_choice)

    """
    Display resume before lunch game
    """
    def game_title_resume(self, p1, p2):
        os_system(self.var_os)

        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("Resume Game"))
        print(" ╠" + "═" * 51 + "╣")
        print(" ║{0:8}{1:10}{2:>24}{0:8}║".format("",
                                                  "Player 1 : ",
                                                  p1))
        print(" ║{0:8}{1:10}{2:>24}{0:8}║".format("",
                                                  "Player 2 : ",
                                                  p2))
        print(" ║{:51}║".format(""))
        print(" ║{0:8}{1:14}{2:>21}{0:8}║".format("",
                                                  "Difficulty : ",
                                                  self.difficulty_list[self.difficulty]))
        print(" ║{0:8}{1:14}{2:>21}{0:8}║".format("",
                                                  "Mod : ",
                                                  self.mod_list[self.mod]))
        print(" ╚" + "═" * 51 + "╝")
        input("  Press Enter to continue...")

    """
    Display colors available
    """
    def view_color(self):
        x = 0

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 16 + "╗")
        print(" ║{:^16}║".format("COLORS"))
        print(" ╠" + "═" * 16 + "╣")
        for color in self.color_list:
            print(" ║ {:2} | {:9} ║".format(x,
                                            color))
            x += 1

        print(" ╚" + "═" * 16 + "╝")

    """
    Display warning before player choose solution
    """
    def game_warning(self):

        os_system(self.var_os)
        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("WARNING"))
        print(" ║{:51}║".format(""))
        print(" ║{:51}║".format(" " + self.players[0].name + ", you will choose the solution"))
        print(" ║{:51}║".format(" Press Enter when you are sure not to be seen !"))
        print(" ╚" + "═" * 51 + "╝")

        input("  Press Enter to continue...")

    """
    Display board game
    """
    def game_board_view(self):
        cpt = 0
        os_system(self.var_os)
        print("")

        if self.difficulty == 1:
            head = " ╔" + "═" * 39 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = " ╠" + "═" * 39 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = " ╚" + "═" * 39 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"

            print(head)

            for color_choice in self.color_choice_save:

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = '------'

                print(" ║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                      "║ {:^3} : {:^3} | {:^3} : {:^3} ║"
                      "║ {:2} | {:9} ║".format(self.color_list[int(color_choice[0])].upper(),
                                               self.color_list[int(color_choice[1])].upper(),
                                               self.color_list[int(color_choice[2])].upper(),
                                               self.color_list[int(color_choice[3])].upper(),
                                               list(self.color_result_save[cpt].keys())[0],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[0]
                                               ],
                                               list(self.color_result_save[cpt].keys())[1],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[1]
                                               ],
                                               cpt,
                                               color.upper()))
                print(middle)
                cpt = cpt + 1

            for i in range(0, 10 - cpt):

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = '------'

                print(" ║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {0:^3}   {0:^3} | {0:^3}   {0:^3} ║"
                      "║ {1:2} | {2:9} ║".format("",
                                                 cpt,
                                                 color.upper()))
                print(middle)
                cpt = cpt + 1

            if self.mod == 2:
                print(
                    " ║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                    "║ {:^9} | {:^9} ║"
                    "║{:^16}║".format(self.color_list[int(self.solution[0])].upper(),
                                      self.color_list[int(self.solution[1])].upper(),
                                      self.color_list[int(self.solution[2])].upper(),
                                      self.color_list[int(self.solution[3])].upper(),
                                      "PLACED",
                                      "COLOR",
                                      "COLORS"))
            else:
                print(" ║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {1:^9} | {2:^9} ║"
                      "║{3:^16}║".format("X",
                                         "COMPLETED",
                                         "PARTIAL",
                                         "COLORS"))

        else:
            head = " ╔" + "═" * 47 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = " ╠" + "═" * 47 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = " ╚" + "═" * 47 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"

            print(head)

            for color_choice in self.color_choice_save:
                if len(self.color_list) >= cpt:
                    color = self.color_list[cpt]
                else:
                    color = ' '

                print(" ║{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}║"
                      "║ {:^3} : {:^3} | {:^3} : {:^3} ║"
                      "║ {:2} | {:9} ║".format(color_choice[0],
                                               color_choice[1],
                                               color_choice[2],
                                               color_choice[3],
                                               color_choice[4],
                                               color_choice[5],
                                               list(self.color_result_save[cpt].keys())[0],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[0]
                                               ],
                                               list(self.color_result_save[cpt].keys())[1],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[1]
                                               ],
                                               cpt,
                                               color.upper()))
                print(middle)
                cpt = cpt + 1

            for i in range(0, 10 - cpt):

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = ' '

                print(" ║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║ {0:^3}   {0:^3} | {0:^3}   {0:^3} ║"
                      "║ {1:2} | {2:9} ║".format("",
                                                 cpt,
                                                 color.upper()))
                print(middle)

                cpt = cpt + 1

            print(middle)

            if self.mod == 2:
                print(
                    " ║{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}║"
                    "║ {:^9} | {:^9} ║"
                    "║{:^16}║".format(self.color_list[int(self.solution[0])].upper(),
                                      self.color_list[int(self.solution[1])].upper(),
                                      self.color_list[int(self.solution[2])].upper(),
                                      self.color_list[int(self.solution[3])].upper(),
                                      self.color_list[int(self.solution[4])].upper(),
                                      self.color_list[int(self.solution[5])].upper(),
                                      "COMPLETED",
                                      "PARTIAL",
                                      "COLORS"))
            else:
                print(" ║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║ {1:^9} | {2:^9} ║"
                      "║{2:^16}║".format("x",
                                         "COMPLETED",
                                         "PARTIAL",
                                         "COLORS"))

        print(foot)

    """
    Verify color choice compared to solution
    """
    def verify_choice(self):
        color_choice = self.color_choice_save[-1]
        solution_copy = self.solution[:]
        result_choice = {"X": 0, "O": 0}

        for cpt1 in range(0, len(solution_copy)):
            if solution_copy[cpt1] == color_choice[cpt1]:
                result_choice['X'] = result_choice['X'] + 1
                solution_copy[cpt1] = " "

        for cpt1 in range(0, len(solution_copy)):

            for cpt2 in range(0, len(solution_copy)):

                if solution_copy[cpt1] == color_choice[cpt2]:
                    result_choice['O'] = result_choice['O'] + 1
                    solution_copy[cpt1] = " "
                    break

        self.color_result_save.append(result_choice)

    """
    Verify if game if player won, loose or if game continue
    """
    def verify_end_game(self):

        if len(self.color_result_save) >= 10:
            self.game_continue = False
        elif len(self.color_result_save) > 0:
            if self.color_result_save[-1]["X"] == len(self.solution):
                self.game_continue = False

    """
    Display result of the game
    """
    def result_game(self):
        os_system(self.var_os)

        if self.color_result_save[-1]["X"] == len(self.solution):
            print("")
            print(" ╔" + "═" * 51 + "╗")
            print(" ║{:^51}║".format("FELICITATION !"))
            print(" ║{:51}║".format(""))
            print(" ║{:^51}║".format(" You won in " + str(len(self.color_result_save)) + " tries"))
            print(" ║{:51}║".format(""))

            self.insert_high_score(len(self.color_result_save))

        if self.color_result_save[-1]["X"] != len(self.solution):
            print("")
            print(" ╔" + "═" * 51 + "╗")
            print(" ║{:^51}║".format("TOO BAD..."))
            print(" ║{:51}║".format(""))
            print(" ║{:51}║".format(" You loose the game, you don't find the solution"))

        print(" ╚" + "═" * 51 + "╝")
        print("")
        print(" ╔" + "═" * 51 + "╗")
        print(" ║{:^51}║".format("SOLUTION"))
        print(" ║{:51}║".format(""))

        if self.difficulty == 1:
            print(" ║ {:^10} | {:^10} | {:^10} | {:^10} ║".format(self.color_list[int(self.solution[0])].upper(),
                                                                  self.color_list[int(self.solution[1])].upper(),
                                                                  self.color_list[int(self.solution[2])].upper(),
                                                                  self.color_list[int(self.solution[3])].upper()
                                                                  ))
        else:
            print(" ║  {:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}  ║".format(self.color_list[int(self.solution[0])].upper(),
                                                                      self.color_list[int(self.solution[1])].upper(),
                                                                      self.color_list[int(self.solution[2])].upper(),
                                                                      self.color_list[int(self.solution[3])].upper(),
                                                                      self.color_list[int(self.solution[4])].upper(),
                                                                      self.color_list[int(self.solution[5])].upper()
                                                                      ))

        print(" ╚" + "═" * 51 + "╝")

        input("  Press enter to continue...")

    """
    Set game_continue to specify if we start new game
    """
    def set_another_game(self):
        rst = ''

        while True:

            if rst == 'y':
                self.solution = []
                self.color_choice_save = []
                self.color_result_save = []
                self.game_continue = True
                self.players = self.players[::-1]
                break

            elif rst == 'n':
                self.game_continue = False
                break

            else:
                rst = str(input("  Another game ? y / n : ")).lower().strip()

    def display_high_score(self):
        x = 0

        try:
            connection = sqlite3.connect("highscore.db")
            cursor = connection.cursor()
            cursor.execute("Select name, score FROM Mastermind ORDER BY score ASC")

            os_system(self.var_os)
            print("")
            print(" ╔" + "═" * 20 + "╗")
            print(" ║{:^20}║".format("HIGHSCORE"))
            print(" ╠" + "═" * 20 + "╣")

            for row in cursor.fetchall():
                print(" ║ {:13} | {:2} ║".format(row[0],
                                                 row[1]))
                if x > 9:
                    break

                x += 1

            print(" ╚" + "═" * 20 + "╝")
            connection.close()

        except Exception as e:
            print('[ERROR] ', e)

    def insert_high_score(self, score):

        try:
            connection = sqlite3.connect("highscore.db")
            cursor = connection.cursor()
            sql = '''INSERT INTO Mastermind (name,score) VALUES (?,?)'''
            cursor.execute(sql, (self.players[1].name, score))
            connection.commit()
            connection.close()

        except Exception as e:
            print('[ERROR] ', e)
