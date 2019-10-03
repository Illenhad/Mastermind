class Player:
    def __init__(self, number):
        self.name = "Player"
        self.player_number = number

    def set_name(self):
        res = True
        name_prop = ""

        while res:
            res = False

            while len(name_prop) < 1:
                name_prop = input(" Player {} Enter your name : ".format(self.player_number))

            for x in name_prop:
                if not (ord("A") <= ord(x) <= ord("Z")) | (ord("a") <= ord(x) <= ord("z")):
                    print(" Enter a name within number or special characters.")
                    res = True
                    break

        self.name = name_prop
