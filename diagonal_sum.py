class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        m = len(A) - 1
        n = len(A[0])
        i = 0
        j = 0
        result = 0
        while i <= m and j <= n:
            result += A[i][j]
            i += 1
            j += 1
        return result


A = [[1, -2, -3],
     [-4, 5, -6],
     [-7, -8, 9]]

A = [[3, 2],
     [2, 3]]

A = [[1, -2, -3],
     [-4, 5, -6],
     [-7, -8, 9]]
obj = Solution()
print(obj.solve(A))