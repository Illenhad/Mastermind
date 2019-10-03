class Game:
    def __init__(self):
        self.color = ['yellow', 'blue', 'red', 'green', 'white', 'black', 'orange', 'violet']
        self.solution = []
        self.difficulty = 0

    def set_color(self, n):
        if n == 2:
            self.color.append('pink')
            self.color.append('grey')

    def set_solution(self):
        while self.solution.count() <= 4:
            solution_choice = ''

            while not (solution_choice in self.color):
                solution_choice = input('Enter a color \n')

            self.append(solution_choice)

    def gameTitle(self):
        print(" ---------------------------------------------------")
        print("|              Welcome to Mastermind !              |")
        print(" ---------------------------------------------------")

    def gameDifficulty(self):
        print(" ---------------------------------------------------")
        print("|            1 : Normal    2 : Difficult            |")
        print(" ---------------------------------------------------")
        difficulty_choice = int(input(" Choose your difficulty : "))

        while difficulty_choice not in (1, 2):
            print(" Enter 1 for Normal or 2 for Difficult.")
            difficulty_choice = int(input(" Choose your difficulty : "))

        self.difficulty = difficulty_choice
