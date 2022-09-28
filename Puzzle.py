from copy import deepcopy


class Puzzle:

    def __init__(self, data: list, expected_state: list, last_state: list = []) -> None:
        self.g = 1
        self.h = 0
        self.f = 0
        self.data = data
        self.expected_state = expected_state
        self.last_state = last_state
        self.possibilities = []
        self.calculate()

    def calculateH(self) -> int:
        h = 0
        if len(self.data) == len(self.expected_state):
            for x, line in enumerate(self.expected_state):
                for y in line:
                    if y != 0:
                        expected_position = self.findSpace(y, True)
                        current_position = self.findSpace(y)

                        x_sum = abs(expected_position[0] - current_position[0])
                        y_sum = abs(expected_position[1] - current_position[1])
                        h += x_sum + y_sum

                        print(f"Y: {y} Expected: {expected_position} Current: {current_position} H: {x_sum + y_sum}\n")
        return h

    def calculate(self):
        self.h = self.calculateH()
        self.g = 1
        self.f = self.h + self.g
        self.measurePossibilities()

    def findSpace(self, spaceFinded, isFinalState: bool = False) -> tuple:
        matriz = self.data if not isFinalState else self.expected_state
        for x, line in enumerate(matriz):
            if spaceFinded in line:
                return (x, line.index(spaceFinded))
        return ()

    def measurePossibilities(self) -> None:
        zero_position = self.findSpace(0)
        x_ = zero_position[0]
        y_ = zero_position[1]

        max_ = len(self.data)
        
        if (x_+1 < max_): self.addPossibilites(self.swapPosition((x_+1, y_)))
        if (x_-1 > -1): self.addPossibilites(self.swapPosition((x_-1, y_)))
        if (y_+1 < max_): self.addPossibilites(self.swapPosition((x_, y_+1)))
        if (y_-1 > -1): self.addPossibilites(self.swapPosition((x_, y_-1)))

    def addPossibilites(self, possibiliti):
        if (possibiliti != []):
            self.possibilities.append(possibiliti)

    def swapPosition(self, new_position):
        result = deepcopy(self.data)
        zero_position = self.findSpace(0)
        x_ = zero_position[0]
        y_ = zero_position[1]

        x = new_position[0]
        y = new_position[1]

        last_value = self.data[x][y]

        result[x][y] = 0
        result[x_][y_] = last_value

        if result != self.last_state: 
            return (result, self.expected_state, self.data)
        return []

    def __str__(self) -> str:
        result = ""
        for i in self.data:
            result += f"{i}\n".replace("[", "|").replace("]", "|").replace(",", "").replace("0", " ")
        result += "\n"
        for i in self.possibilities:
            result += f"{i}"
        return result

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

matriz_b = [
    [8, 7, 6],
    [3, 2, 1],
    [5, 0, 4]
]

p = Puzzle(matriz_b, matriz_a)
p.calculate()
print(p)
print(p.h)
