class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        print(range(len(self.matrix)))


    def __add__(self, other):
        if self.check == other.check:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    return self.matrix[i][j] + other.matrix[i][j]

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    @property
    def check(self):
        rows = len(self.matrix)
        columns = 0
        for row in self.matrix:
            if len(row) > columns:
                columns = len(row)

        return rows, columns


a = Matrix([[1, 1, 1], [0, 0, 0]])
b = Matrix([[2, 2, 2], [4, 5, 4], [34, 45, 23]])
print(a)
print('------')
print(b)
print(a + b)
