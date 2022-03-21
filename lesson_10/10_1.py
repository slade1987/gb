class Matrix:
    sizeI = 0
    sizeJ = 0
    matrix = []
    def __init__(self,mat):
        self.sizeI = len(mat)
        self.sizeJ = len(mat[0])
        self.matrix = mat

    def __str__(self):
        str_mat =''
        for i in range(self.sizeI):
            for j in range(self.sizeJ):
                str_mat = str(str_mat) + ' ' + str(self.matrix[i][j])
            str_mat = str_mat + '\n'
        return str_mat

    def __add__(self, other):
        str_mat = ''
        if self.sizeI == other.sizeI:
            for i in range(self.sizeI):
                for j in range(self.sizeJ):
                    str_mat = str(str_mat) + ' ' + str(self.matrix[i][j] + other.matrix[i][j])
                str_mat = str_mat + '\n'
        return str_mat



matr = Matrix([[1,2,3],[1,2,3],[1,2,3]])
matr1 = Matrix([[1,2,3],[1,2,3],[1,2,3]])
matr2 = matr + matr1
print(matr2)