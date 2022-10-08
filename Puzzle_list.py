from copy import deepcopy
from os import stat
from unittest import result

class Puzzle:

    def __init__(self, data: list, expected_state: list) -> None:
        self.g = 0
        self.h = 0
        self.f = 0
        self.data = data
        self.expected_state = expected_state
        self.current_game = []

    def calculateH(self, state: list) -> int:
        h = 0
        if len(self.data) == len(self.expected_state):
            for x, line in enumerate(state):
                for y in line:
                    if y != 0:
                        expected_position = self.findSpace(y, self.expected_state)
                        current_position = self.findSpace(y, state)

                        x_sum = abs(expected_position[0] - current_position[0])
                        y_sum = abs(expected_position[1] - current_position[1])
                        h += x_sum + y_sum
                        #print(f"Y: {y} Expected: {expected_position} Current: {current_position} H: {x_sum + y_sum}\n")
        return h    

    def findSpace(self, spaceFinded, state: list) -> tuple:
        for x, line in enumerate(state):
            if spaceFinded in line:
                return (x, line.index(spaceFinded))
        return ()
        
    def measurePossibilities(self, state: list) -> list:
        zero_position = self.findSpace(0, state)
        possibilites = []
        x_ = zero_position[0]
        y_ = zero_position[1]

        max_ = len(state)
        
        if (x_+1 < max_): possibilites.append(self.swapPosition(state, (x_+1, y_)))
        if (x_-1 > -1): possibilites.append(self.swapPosition(state, (x_-1, y_)))
        if (y_+1 < max_): possibilites.append(self.swapPosition(state, (x_, y_+1)))
        if (y_-1 > -1): possibilites.append(self.swapPosition(state, (x_, y_-1)))

        return possibilites
        
    def swapPosition(self, state: list, new_position: tuple) -> list:
        result = deepcopy(state)
        zero_position = self.findSpace(0, result)
        x_ = zero_position[0]
        y_ = zero_position[1]

        x = new_position[0]
        y = new_position[1]

        last_value = state[x][y]

        result[x][y] = 0
        result[x_][y_] = last_value

        return result

    def printState(self, state: list) -> None:
        result = ""
        for i in state:
            result += f"{i}\n".replace("[", "|").replace("]", "|").replace(",", "").replace("0", " ")
        result += "\n"
        print(result)

    def getMinStates(self, last_states: list, states: list) -> list:
        #states = Lista contendo os estados
        if len(states) < 2: return states
        current_min = 0
        for pos, state in enumerate(states):
            if state not in last_states:
                h = self.calculateH(state)
                if pos == 0:
                    current_min = h
                if h < current_min:
                    current_min = h

        mins = []
        for state in states:
            if self.calculateH(state) == current_min: mins.append(state)

        return mins

    def interableMatriz(self):

        count = 0
        self.current_game.append(
            self.measurePossibilities(
                self.data
            )
        )

        while True:
            nodes = self.current_game[count]

            if self.expected_state in nodes:
                break

            # Possibilidades do nó atual
            possibilites = []
            for state in nodes:
                for possibilite in self.measurePossibilities(state):
                    possibilites.append(possibilite)

            mins = self.getMinStates(nodes, possibilites)
            self.current_game.append(mins)

            # Níveis da arvore
            count += 1
        
        self.printCurrentGame()

    def printCurrentGame(self):
        for pos, node in enumerate(self.current_game):
            print(f"Nó da Arvore: {pos}")
            for state in node:
                self.printState(state)

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

matriz_b = [
    [0, 8, 2],
    [1, 4, 3],
    [7, 6, 5]
]

p = Puzzle(matriz_b, matriz_a)
p.interableMatriz()