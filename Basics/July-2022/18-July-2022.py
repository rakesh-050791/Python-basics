# 1 : Add the matrices

# You are given two matrices A & B of same size, 
# you have to return another matrix which is the sum of A and B.

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] += B[i][j]
        return A        


# 2 : Anti Diagonals
# Give a N * N square matrix A, return an array of its anti-diagonals. 
# Look at the example for more details.
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        res=[[0]*n for r in range(2*n-1)]
        for j in range(n):
            x , y = 0, j 
            while(x < n and y >= 0):
                res[x+y][x] = A[x][y]
                x += 1
                y -= 1

        for i in range(1, n):
            x, y, l = i, n-1, 0

            while(x < n and y >= 0):
                res[x+y][l] = A[x][y]
                x += 1
                y -= 1
                l += 1
        return res
