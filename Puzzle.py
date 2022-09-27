class Puzzle:

    def __init__(self, data: list, expected_state: list) -> None:
        self.g = 0
        self.h = 0
        self.f = 0
        self.data = data
        self.expected_state = expected_state

    def calculateH(self):
        if len(self.data) == len(self.expected_state):
            for x, line in enumerate(self.expected_state):
                for y in line:
                    expected_position = self.findSpace(y, True)
                    current_position = self.findSpace(y)

                    print(f"Y: {y} Expected: {expected_position} Current: {current_position}\n")

    def findSpace(self, spaceFinded, isFinalState: bool = False) -> tuple:
        matriz = self.data if not isFinalState else self.expected_state
        print(matriz)
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
p.calculateH()
