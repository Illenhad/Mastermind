import os


class Game:
    def __init__(self):
        self.color = ['yellow', 'blue', 'red', 'green', 'white', 'black', 'orange', 'violet']
        self.solution = ["R", "G", "B", "Y"]
        self.difficulty = 0
        self.mod = 0

        # verify OS to clear shell
        if os.name == 'posix':
            self.var_os = 'clear'
        else:
            self.var_os = 'cls'

    def game_title(self):
        os.system(self.var_os)
        print("")
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("Welcome to Mastermind !"))
        print("|{:51}|".format(""))
        print("|{:51}|".format(" For a better experience, we recommend you"))
        print("|{:51}|".format(" to run this program in a real terminal,"))
        print("|{:51}|".format(" not a python interpreter."))
        print(" ---------------------------------------------------")
        input("Press Enter to continue...")

        os.system(self.var_os)
        print("")
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("Player Name"))
        print(" ---------------------------------------------------")

    def game_difficulty(self):
        os.system(self.var_os)
        print("")
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("1 : Normal    2 : Difficult"))
        print(" ---------------------------------------------------")

        while True:
            difficulty_choice = input(" Choose your difficulty : ")

            if len(difficulty_choice) > 0:
                if int(ord(difficulty_choice)) in (49, 50):
                    break

            print(" Enter 1 for Normal or 2 for Difficult.")

        self.difficulty = int(difficulty_choice)

        if self.difficulty == 2:
            self.color.append('pink')
            self.color.append('cyan')

    def game_mod(self):
        res = False

        os.system(self.var_os)
        print("")
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("1 : Normal    2 : Debug"))
        print(" ---------------------------------------------------")

        while True:
            mod_choice = input(" Choose your mod : ")

            if len(mod_choice) > 0:
                if int(ord(mod_choice)) in (49, 50):
                    break

            print(" Enter 1 for Normal or 2 for Debug.")

        self.mod = int(mod_choice)

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
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("Resume Game"))
        print(" ---------------------------------------------------")
        print("|{:8}{:10}{:>24}{:8}|".format("", "Player 1 : ", p1, ""))
        print("|{:8}{:10}{:>24}{:8}|".format("", "Player 2 : ", p2, ""))
        print("|{:51}|".format(""))
        print("|{:8}{:14}{:>21}{:8}|".format("", "Difficulty : ", difficulty_choice, ""))
        print("|{:8}{:14}{:>21}{:8}|".format("", "Mod : ", mod_choice, ""))
        print(" ---------------------------------------------------")
        input("Press Enter to continue...")

    def game_board_view(self, color_choice_save, color_result_save):
        x = 0
        os.system(self.var_os)

        if self.difficulty == 1:
            head = "╔" + "═" * 33 + "╦" * 2 + "═" * 16 + "╗"
            middle = "╠" + "═" * 33 + "╬" * 2 + "═" * 16 + "╣"
            foot = "╚" + "═" * 33 + "╩" * 2 + "═" * 16 + "╝"
            print(head)

            for color_choice in color_choice_save:
                print("║ {:^7}|{:^7}|{:^7}|{:^7} ║║ {:^3}|{:^3}|{:^3}|{:^3}║".format(color_choice[0],
                                                                                     color_choice[1],
                                                                                     color_choice[2],
                                                                                     color_choice[3],
                                                                                     color_result_save[x][0],
                                                                                     color_result_save[x][1],
                                                                                     color_result_save[x][2],
                                                                                     color_result_save[x][3]))
                print(middle)
                x = x + 1

            for i in range(0, 10 - x):
                print("║ {0:^7}|{0:^7}|{0:^7}|{0:^7} ║║ {0:^3}|{0:^3}|{0:^3}|{0:^3}║".format(""))
                print(middle)

            if self.mod == 2:
                print(
                    "║ {:^7}|{:^7}|{:^7}|{:^7} ║║ {:^15}║".format(self.solution[0], self.solution[1], self.solution[2],
                                                                  self.solution[3], "SOLUTION"))
            else:
                print("║ {0:^7}|{0:^7}|{0:^7}|{0:^7} ║║ {1:^15}║".format("x", "SOLUTION"))

        else:
            head = "╔" + "═" * 49 + "╦" * 2 + "═" * 24 + "╗"
            middle = "╠" + "═" * 49 + "╬" * 2 + "═" * 24 + "╣"
            foot = "╚" + "═" * 49 + "╩" * 2 + "═" * 24 + "╝"
            print(head)

            for color_choice in color_choice_save:
                print("║ {:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7} ║║ {:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}║"
                      .format(color_choice[0], color_choice[1], color_choice[2], color_choice[3], color_choice[4],
                              color_choice[5], color_result_save[x][0], color_result_save[x][1],
                              color_result_save[x][2], color_result_save[x][3], color_result_save[x][4],
                              color_result_save[x][5]))
                print(middle)
                x = x + 1

            for i in range(0, 10 - x):
                print("║ {0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7} ║║ {0:^3}|{0:^3}|{0:^3}|{0:^3}|{0:^3}|{0:^3}║"
                      .format(""))
                print(middle)

            if self.mod == 2:
                print(
                    "║ {:^7}|{:^7}|{:^7}|{:^7} ║║ {:^15}║".format(self.solution[0], self.solution[1], self.solution[2],
                                                                  self.solution[3], self.solution[4], self.solution[5],
                                                                  "SOLUTION"))
            else:
                print("║ {0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7} ║║ {1:^23}║".format("x", "SOLUTION"))

        print(foot)
