class Player :
    
    playerCounter = 0
    
    def __init__(self, name) :
        self._name = name
        self._idPlayer = Player.playerCounter + 1
    
    @property
    def idPlayer(self) :
        return self._idPlayer
    
    @property
    def name(self) :
        return self._name
    
    @name.setter
    def name(self, name) :
        self._name = name
    
    # Functions
    def write_file(self) :
        file = open("./score.txt", "a")
        file.write(f"Id: {self._idPlayer}   Name: {self._name}" + "\n")
        file.close()
    
    def print_file(self) :
        file = open("./score.txt", "r")
        content = file.readlines()
        for lines in content :
            stripped_lines = lines.strip()
            print(stripped_lines)
    
    # toString
    def __str__(self) :
        return f"IdPlayer: {self._idPlayer}, Name: {self._name}."

player1 = Player("solrac")
# player1.write_file()
player1.print_file()