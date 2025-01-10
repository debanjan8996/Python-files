def diagonalDifference(arr):
    
  n = len(arr)
  left_diagonal_sum = 0
  right_diagonal_sum = 0

  for i in range(n):
    left_diagonal_sum += arr[i][i]
    right_diagonal_sum += arr[i][n - i - 1]

  return abs(left_diagonal_sum - right_diagonal_sum)

matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(matrix)
result = diagonalDifference(matrix)
print(result)
