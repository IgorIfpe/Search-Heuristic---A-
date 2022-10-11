from copy import deepcopy
from re import I
from time import sleep
from tkinter import *
import _thread as th

class Puzzle:

    def __init__(self, data: list, expected_state: list) -> None:
        self.g = 0
        self.h = 0
        self.f = 0
        self.data = data
        self.expected_state = expected_state
        self.current_game = [
                [ self.data ]
            ]
        self.count = 0

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

        """print(self.count)
        for i in possibilites:
            self.printState(i)"""

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

    def isAddState(self, state: list) -> bool:
        if state in self.current_game[self.count]:
            return False
        """if len(self.current_game) > 2:
            if state in self.current_game[self.count-1]:
                return False"""
        return True

    def getMinStates(self, states: list) -> list:
        
        #states = Lista contendo os estados
        if len(states) < 2: return states
        
        current_min = 0
        for pos, state in enumerate(states):
            if self.isAddState(state):
                h = self.calculateH(state)
                if pos == 0:
                    current_min = h
                if h < current_min:
                    current_min = h

        mins = []
        for state in states:
            if self.isAddState(state) and state not in mins:
                if self.calculateH(state) == current_min: mins.append(state)
        
        return mins

    def interableMatriz(self):

        while True:
            nodes = self.current_game[self.count]
            self.printCurrentGame()
            if self.expected_state in nodes:
                break

            # Possibilidades do nó atual
            possibilites = []
            for state in nodes:
                for possibilite in self.measurePossibilities(state):
                    possibilites.append(possibilite)
            
            mins = self.getMinStates(possibilites)
            self.current_game.append(mins)

            # Níveis da arvore
            self.count += 1
        
        self.printCurrentGame()

    def printCurrentGame(self):
        for pos, node in enumerate(self.current_game):
            print(f"Nó da Arvore: {pos}")
            for state in node:
                print(f"H: {self.calculateH(state)}")
                self.printState(state)

class PuzzleView:

    def __init__(self, states: list) -> None:
        self.states = states
        self.size = len(self.states[0])
        self.elements = [["" for j in range(self.size)] for i in range(self.size)]
        self.window = Tk()
        self.createWindow()

    def createWindow(self) -> None:
        self.window.geometry("460x700")
        self.window.title("Puzzle View")

        button = Button(text="Start", command=lambda: th.start_new_thread(self.initGame, ()))
        button.pack()

        self.createPuzzleSpaces()

        self.window.mainloop()

    def initGame(self) -> None:

        for state in self.states:
            self.nextPosition(state)
            sleep(1)

    def createPuzzleSpaces(self):
        x_ = 50

        for i in range(self.size):
            y_ = 50
            for j in range(self.size):
                self.elements[i][j] = {
                        "x": x_,
                        "y": y_,
                        "element": self.createPuzzleButton()
                    }
                self.elements[i][j]["element"].place(x = x_, y = y_)
                y_ += 200
            x_ += 120

    def createPuzzleButton(self) -> Button:
        return Button(text="", font="Arial 15", width=10, height=8)
    
    def nextPosition(self, state: list):
        print(state)
        for i in range(self.size):
            for j in range(self.size):
                self.elements[i][j]["element"]["text"] = ""
                if state[j][i] != 0:
                    self.elements[i][j]["element"]["text"] = state[j][i]

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

matriz_c = [
    [7, 2, 8],
    [4, 1, 5],
    [0, 3, 6]
]

solucao = [
    [[5, 2, 8], [4, 1, 7], [0, 3, 6]]
    ,
    [[5, 2, 8], [0, 1, 7], [4, 3, 6]]
    ,
    [[5, 2, 8], [1, 0, 7], [4, 3, 6]]
    ,
    [[5, 2, 8], [1, 7, 0], [4, 3, 6]]
    ,
    [[5, 2, 8], [1, 7, 6], [4, 3, 0]]
    ,
    [[5, 2, 8], [1, 7, 6], [4, 0, 3]]
    ,
    [[5, 2, 8], [1, 0, 6], [4, 7, 3]]
    ,
    [[5, 2, 8], [1, 6, 0], [4, 7, 3]]
    ,
    [[5, 2, 0], [1, 6, 8], [4, 7, 3]]
    ,
    [[5, 0, 2], [1, 6, 8], [4, 7, 3]]
    ,
    [[0, 5, 2], [1, 6, 8], [4, 7, 3]]
    ,
    [[1, 5, 2], [0, 6, 8], [4, 7, 3]]
    ,
    [[1, 5, 2], [4, 6, 8], [0, 7, 3]]
    ,
    [[1, 5, 2], [4, 6, 8], [7, 0, 3]]
    ,
    [[1, 5, 2], [4, 0, 8], [7, 6, 3]]
    ,
    [[1, 5, 2], [4, 8, 0], [7, 6, 3]]
    ,
    [[1, 5, 2], [4, 8, 3], [7, 6, 0]]
    ,
    [[1, 5, 2], [4, 8, 3], [7, 0, 6]]
    ,
    [[1, 5, 2], [4, 0, 3], [7, 8, 6]]
    ,
    [[1, 0, 2], [4, 5, 3], [7, 8, 6]]
    ,
    [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
    ,
    [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
    ,
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
]

p = Puzzle(matriz_c, matriz_a)

PuzzleView(solucao)