n = int(input())
numbers =list(map(int, input().split()))
num = 0 

for i in range(n):
    num += numbers[i]/max(numbers)*100

print(num/n)