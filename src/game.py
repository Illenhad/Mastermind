import os


class Game:
    def __init__(self):
        self.color_list = ['Yellow', 'Pink', 'Red', 'Aqua', 'White', 'Black', 'Orange', 'Violet']
        self.solution = ["R", "G", "B", "Y"]
        self.difficulty_list = {1: "Normal", 2: "Difficult"}
        self.difficulty = 1
        self.mod_list = {1: "Normal", 2: "Debug"}
        self.mod = 1
        self.color_choice_save = []
        self.color_result_save = []

        # Verify OS to clear shell
        if os.name == 'posix':
            self.var_os = 'clear'
        else:
            self.var_os = 'cls'

    def game_title(self):
        os.system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Welcome to Mastermind !"))
        print("║{:51}║".format(""))
        print("║{:51}║".format(" For a better experience, we recommend you"))
        print("║{:51}║".format(" to run this program in a real terminal,"))
        print("║{:51}║".format(" not a python interpreter."))
        print("╚" + "═" * 51 + "╝")
        input("Press Enter to continue...")

        os.system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Player Name"))
        print("╚" + "═" * 51 + "╝")

    # Set self.difficulty
    # Difficult : add two colors into color list
    def game_difficulty(self):
        res = ""

        os.system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")

        for difficulty in self.difficulty_list:
            res = res + "{:^} : {:^}  ".format(difficulty, self.difficulty_list[difficulty])

        print("║{:^51}║".format(res))
        print("╚" + "═" * 51 + "╝")

        while True:
            difficulty_choice = input(" Choose your difficulty : ")

            if len(difficulty_choice) == 1:
                if int(ord(difficulty_choice)) in (49, 50):
                    break

            print(" Enter 1 for Normal or 2 for Difficult.")

        self.difficulty = int(difficulty_choice)

        if self.difficulty == 2:
            self.color_list.append('Gold')
            self.color_list.append('Silver')

        self.color_list.sort()

    # Set self.mod
    # Normal : Solution is hidden
    # Debug : Solution is visible
    def set_mod(self):
        res = ""

        os.system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")

        for mod in self.mod_list:
            res = res + "{:^} : {:^}  ".format(mod, self.mod_list[mod])

        print("║{:^51}║".format(res))
        print("╚" + "═" * 51 + "╝")

        while True:
            mod_choice = input(" Choose your mod : ")

            if len(mod_choice) > 0:
                if int(ord(mod_choice)) in (49, 50):
                    break

            print(" Enter 1 for Normal or 2 for Debug.")

        self.mod = int(mod_choice)

    # Print resume before lunch game
    #
    def game_title_resume(self, p1, p2):
        os.system(self.var_os)

        if self.difficulty == 1:
            difficulty_choice = "Normal"
        else:
            difficulty_choice = "Difficult"

        if self.mod == 1:
            mod_choice = "Normal"
        else:
            mod_choice = "Difficult"

        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Resume Game"))
        print("╠" + "═" * 51 + "╣")
        print("║{:8}{:10}{:>24}{:8}║".format("", "Player 1 : ", p1, ""))
        print("║{:8}{:10}{:>24}{:8}║".format("", "Player 2 : ", p2, ""))
        print("║{:51}║".format(""))
        print("║{:8}{:14}{:>21}{:8}║".format("", "Difficulty : ", difficulty_choice, ""))
        print("║{:8}{:14}{:>21}{:8}║".format("", "Mod : ", mod_choice, ""))
        print("╚" + "═" * 51 + "╝")
        input("Press Enter to continue...")

    def game_board_view(self):
        x = 0
        os.system(self.var_os)
        print(" ")

        if self.difficulty == 1:
            head = "╔" + "═" * 39 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = "╠" + "═" * 39 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = "╚" + "═" * 39 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"

            print(head)

            for color_choice in self.color_choice_save:

                if len(self.color_list) > x:
                    color = self.color_list[x]
                else:
                    color = '------'

                print("║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                      "║ {:^3} | {:^3} | {:^3} | {:^3} ║"
                      "║ {:2} | {:9} ║".format(self.color_list[int(color_choice[0])].upper(),
                                               self.color_list[int(color_choice[1])].upper(),
                                               self.color_list[int(color_choice[2])].upper(),
                                               self.color_list[int(color_choice[3])].upper(),
                                               self.color_result_save[x][0],
                                               self.color_result_save[x][1],
                                               self.color_result_save[x][2],
                                               self.color_result_save[x][3],
                                               x,
                                               color.upper()))
                print(middle)
                x = x + 1

            for i in range(0, 10 - x):

                if len(self.color_list) > x:
                    color = self.color_list[x]
                else:
                    color = '------'

                print("║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {0:^3} | {0:^3} | {0:^3} | {0:^3} ║"
                      "║ {1:2} | {2:9} ║".format("",
                                                 x,
                                                 color.upper()))
                print(middle)
                x = x + 1

            if self.mod == 2:
                print(
                    "║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                    "║ {:^21} ║"
                    "║{:^16}║".format(self.solution[0],
                                      self.solution[1],
                                      self.solution[2],
                                      self.solution[3],
                                      "SOLUTION",
                                      "COLORS"))
            else:
                print("║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {1:^21} ║"
                      "║{2:^16}║".format("x",
                                         "SOLUTION",
                                         "COLORS"))

        else:
            head = "╔" + "═" * 47 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = "╠" + "═" * 47 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = "╚" + "═" * 47 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"
            print(head)

            for color_choice in self.color_choice_save:
                if len(self.color_list) >= x:
                    color = self.color_list[x]
                else:
                    color = ' '

                print("║{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}║"
                      "║{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}║"
                      "║ {:2} | {:9} ║".format(color_choice[0],
                                               color_choice[1],
                                               color_choice[2],
                                               color_choice[3],
                                               color_choice[4],
                                               color_choice[5],
                                               self.color_result_save[x][0],
                                               self.color_result_save[x][1],
                                               self.color_result_save[x][2],
                                               self.color_result_save[x][3],
                                               self.color_result_save[x][4],
                                               self.color_result_save[x][5],
                                               x,
                                               color.upper()))
                print(middle)
                x = x + 1

            for i in range(0, 10 - x):

                if len(self.color_list) > x:
                    color = self.color_list[x]
                else:
                    color = ' '

                print("║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║{0:^3}|{0:^3}|{0:^3}|{0:^3}|{0:^3}|{0:^3}║"
                      "║ {1:2} | {2:9} ║".format("---",
                                                 x,
                                                 color.upper()))
                print(middle)

                x = x + 1

            print(middle)

            if self.mod == 2:
                print(
                    "║{:^7}|{:^7}|{:^7}|{:^7}║"
                    "║{:^15}║".format(self.solution[0],
                                       self.solution[1],
                                       self.solution[2],
                                       self.solution[3],
                                       self.solution[4],
                                       self.solution[5],
                                       "SOLUTION"))
            else:
                print("║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║{1:^23}║"
                      "║{2:^16}║".format("x",
                                         "SOLUTION",
                                         "COLORS"))

        print(foot)
