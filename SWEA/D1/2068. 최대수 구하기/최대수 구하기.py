t = int(input())
for i in range(1,t+1):
    numbers = list(map(int,input().split()))
    num = max(numbers)
    print(f'#{i} {num}')