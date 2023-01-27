arr = [] 
for i in range(10):
    num = int(input())
    arr.append(num % 42)
arr = set(arr) # set 중복제거
print(len(arr))
