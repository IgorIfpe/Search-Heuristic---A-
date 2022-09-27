class Puzzle:

    def __init__(self, data: list, expected_state: list) -> None:
        self.g = 1
        self.h = 0
        self.f = 0
        self.data = data
        self.expected_state = expected_state
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

    def findSpace(self, spaceFinded, isFinalState: bool = False) -> tuple:
        matriz = self.data if not isFinalState else self.expected_state
        for x, line in enumerate(matriz):
            if spaceFinded in line:
                return (x, line.index(spaceFinded))
        return ()

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
print(p.h)
