def sort_in_wave(arr):
  n = len(arr)

  arr.sort()

  for i in range(0, n-1, 2):
    if i > 0 and arr[i-1] > arr[i]:
      arr[i-1], arr[i] = arr[i], arr[i-1]
    if i < n-2 and arr[i] < arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]

  return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80]
print(sort_in_wave(arr))
