"""
===============================================================================

Description  : Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
===============================================================================
SOLUTION  :

[[1,1,1], 0
 [1,0,1], 1
 [1,1,1]] m
  0 1 n
m = len(matrix) = lenght of column, i.e. number of rows
n = len(matrix[0]) = lenght of row, i.e. number of columns

Use the first row and first column as markers to keep track of which rows and columns need to be set to zero.
First, check if the first row and first column need to be zeroed out. 
Second, iterate through the rest of the matrix. 
Mark the first row and the first column elements as 0 if you encounter a zero.
Finally, use these markers to set the appropriate elements to zero. 
This approach allows to solve the problem in-place without using extra space.
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix.
"""

def setZeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check if first row needs to be zeroed. Fix the column and iterate through the row.
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column needs to be zeroed. Fix the row and iterate through the column.
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Use first row and column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set zeroes based on markers
    for i in range(1, m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Zero out first row if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Zero out first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print (matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print (matrix)