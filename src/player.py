class Player:
    def __init__(self, number):
        self.name = "Player"
        self.number = number

    def set_name(self):
        res = True

        while res:
            name_prop = input(" Player {} Enter your name : ".format(self.number))
            res = False

            for x in name_prop:
                if not (ord("A") <= ord(x) <= ord("Z")) | (ord("a") <= ord(x) <= ord("z")):
                    print("Enter a name within number or special characters.")
                    res = True
                    break

        self.name = name_prop
