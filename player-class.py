class Player :
    
    playerCounter = 0
    
    def __init__(self, name) :
        self._name = name
        Player.playerCounter += 1
    
    @property
    def name(self) :
        return self._name
    
    @name.setter
    def name(self, name) :
        self._name = name
    
    # Functions
    def write_file(self) :
        file = open("./score.txt", "a")
        file.write(f"Id: {Player.playerCounter}   Name: {self._name}" + "\n")
        file.close()
    
    def print_file(self) :
        file = open("./score.txt", "r")
        content = file.readlines()
        for lines in content :
            stripped_lines = lines.strip()
            print(stripped_lines)
    
    # toString
    def __str__(self) :
        return f"IdPlayer: {Player.playerCounter}, Name: {self._name}."

player1 = Player("solrac")
# player1.write_file()
player1.print_file()

player2 = Player("Rozk")
# player2.write_file()

player3 = Player("ElJezeverth")
# player3.write_file()