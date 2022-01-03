def rev(arr):
  n = len(arr)
  # [1,2,3,4,5]
  for i in range(n//2):
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    
    
arr = [int(i) for i in input().split()]
rev(arr)
print(*arr)    
