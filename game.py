import os


class Game:
    def __init__(self):
        self.color = ['yellow', 'blue', 'red', 'green', 'white', 'black', 'orange', 'violet']
        self.solution = []
        self.difficulty = 0
        self.mod = 0

        # verify OS to clear shell
        if os.name == 'posix':
            self.var_os = 'clear'
        else:
            self.var_os = 'cls'

    def set_color(self, n):

        if n == 2:
            self.color.append('pink')
            self.color.append('cyan')

    def set_solution(self):

        while self.solution.count() <= 4:
            solution_choice = ''

            while not (solution_choice in self.color):
                solution_choice = input('Enter a color \n')

            self.append(solution_choice)

    def game_title(self):
        os.system(self.var_os)
        print("")
        print(" ---------------------------------------------------")
        print("|{:^51}|".format("Welcome to Mastermind !"))
        print("|{:51}|".format(""))
        print("|{:51}|".format(" For a better experience, we recommend you"))
        print("|{:51}|".format(" to run this program in a real terminal,"))
        print("|{:51}|".format(" not an python interpreter."))
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

    def game_choice_color(self):
        select = 0
        count_select = 0
        color_choice = []

        if self.difficulty == 1:
            cases = 4
        if self.difficulty == 2:
            cases = 6

        for number, letter in enumerate(self.color):
            print(number, " ", letter, end=" ")

        print("\n Choose a number ", cases, " times, each number is a color")

        while int(select) <= int(number) and count_select < cases:
            select = input("Choose a color's number ")
            color_choice.append(select)
            count_select = count_select + 1

        for select in color_choice:
            print(self.color[int(select)])
        input("tape sur entrée")

        # else:
        #     print(enumerate(self.color), end=" ")
        #     print("Choose a number 6 times, each number is a color")
        #
        #     while count_select < 6:
        #
        #         if select in self.color.count():
        #             select = input("Choose a color's number ", end=" ")
        #             color_choice.append(select)
        #             count_select += count_select
        #             print(select)