import numpy

class gameData:
    def __init__(self):
        self.data = self.initData()

    def initData(self): return numpy.zeros((3,3))

    def set_data(self, pos, data): self.data[pos[0]][pos[1]] = data

    def isWinner(self):
        for i in range(3):
            horizontal = len(set(self.data[i])) == 1
            vertical = len(set(self.data[i][0], self.data[i][1], self.data[i][2]))
            diagonal = len(set(self.data[i][i]))
            if vertical or horizontal:
                return True
                
