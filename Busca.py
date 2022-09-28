import random

class Game:

    def __init__(self) -> None:
        self.final_state = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]
                    ]

        self.start_state = []
        self.random()

    def random(self) -> None:
        new_matriz = self.final_state.copy()
        
        for line in new_matriz:
            random.shuffle(line)
            self.start_state.append(line)

    def getCurrentState(self) -> list:
        return self.start_state

    def printCurrentState(self) -> None:
        for line in self.start_state:
            print(line)

    def nextPosition(self):
        pos = self.findSpace(1)
        final_pos = self.findSpace(1, True)
        print(pos, final_pos)
        #self.printCurrentState()

    def updateCurrentState(self, value, x, y) -> None:
        pass

    def findSpace(self, spaceFinded, isFinalState=False) -> dict:
        matriz = self.final_state if isFinalState else self.start_state
        for pos, line in enumerate(matriz):
            if spaceFinded in line:
                return {'line': pos, 'pos': line.index(spaceFinded)}

        return {}

game = Game()
game.printCurrentState()
print(game.findSpace(7))
game.nextPosition()
