class Player:
    def __init__(self, number):
        self.name = "Player"
        self.player_number = number

    def set_name(self):
        res = True

        while res:
            res = False
            name_prop = input(" Player {} Enter your name : ".format(self.player_number))

            if len(name_prop) > 0:

                for x in name_prop:
                    if not (ord("A") <= ord(x) <= ord("Z")) | (ord("a") <= ord(x) <= ord("z")):
                        print(" Enter a name within number or special characters.")
                        res = True
                        break
            else:
                print(" Enter a name within number or special characters.")
                res = True

        self.name = name_prop

    def select_colors(self, color_list):
        color_choice = []

        if len(color_list) == 8:
            cases = 4
        else:
            cases = 6

        while len(color_choice) < cases:

            while True:
                select = input(" Choose your color : ")

                if len(select) == 1:
                    if int(ord("0")) <= int(ord(select)) <= int(ord(str(len(color_list) - 1))):
                        break

                print(" Enter the number before color.")

            color_choice.append(select)

        input("Press enter to continue...")

        return color_choice
