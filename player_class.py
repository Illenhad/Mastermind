class Player:
    def __init__(self, number):
        self.name = "Player"
        self.player_number = number

    """
    Set name of player
    """
    def set_name(self):
        res = True
        name_prop = ""

        while res:
            res = False
            name_prop = input("  Player {} Enter your name : ".format(self.player_number))

            if len(name_prop) > 0:

                for x in name_prop:
                    if not (ord("A") <= ord(x) <= ord("Z")) | (ord("a") <= ord(x) <= ord("z")):
                        print("  Enter a name within number or special characters.\n")
                        res = True
                        break
            else:
                print("  Enter a name within number or special characters.\n")
                res = True

        self.name = name_prop

    """
    Player choose color from a list
    """
    def select_colors(self, color_list):
        color_choice = []
        x = 1

        if len(color_list) == 8:
            cases = 4
        else:
            cases = 6

        while len(color_choice) < cases:

            while True:
                select = input("  {}, choose color {}: ".format(self.name,
                                                                x))

                if len(select) == 1:
                    if int(ord("0")) <= int(ord(select)) <= int(ord(str(len(color_list) - 1))):
                        break

                print("  Enter the number before color.\n")

            color_choice.append(select)
            x += 1

        input("\n  Press enter to continue...")

        return color_choice
