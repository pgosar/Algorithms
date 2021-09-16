class Solution:
    def spiralOrder(self, matrix):

        arr = []
        rowStart = 0
        colStart = 0
        rowEnd = len(matrix)-1
        colEnd = len(matrix[0])-1
       
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                arr.append(matrix[rowStart][i])
            rowStart+=1
            for i in range(rowStart, rowEnd+1):
                arr.append(matrix[i][colEnd])
            colEnd -= 1
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart-1, -1):
                    arr.append(matrix[rowEnd][i])
                rowEnd-=1
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart-1, -1):
                    arr.append(matrix[i][colStart])
                colStart+=1

        return arr

