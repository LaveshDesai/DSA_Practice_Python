arr = list(map(int,input().split()))
mx = max(arr)

while mx in arr:
  arr.remove(mx)
print(max(arr))
