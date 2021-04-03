class Matrix:
    def __init__(self, matrix_string):
        self.row = [[int(x) for x in i.split(' ')] for i in matrix_string.splitlines()]

    def row(self, index):
        return self.row[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.row]
