class Player:
    def __init__(self):
        self.name = "Pierre"
        for x in self.name:
            if not (ord('A') <= ord(x) <= ord('Z')) | (ord('a') <= ord(x) <= ord('z')):
                print("erreur")
                break
            else:
                print(x, end='')

    def set_name(self):
        self.name = input("Enter your name")
