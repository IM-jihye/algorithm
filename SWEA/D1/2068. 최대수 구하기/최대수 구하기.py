T = int(input())
for t in range(1, T+1):
     numbers = list(map(int,input().split()))
     numbers = max(numbers)
     print(f"#{t} {numbers}")