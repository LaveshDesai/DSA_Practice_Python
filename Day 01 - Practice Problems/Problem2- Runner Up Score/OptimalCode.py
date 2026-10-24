first  = float('-inf')
second = float('-inf')

arr = list(map(int,input().split()))

for num in arr:
  if num>first:
    second = first
    first = num

  elif first>num>second:
    second = num

print(second)


    
