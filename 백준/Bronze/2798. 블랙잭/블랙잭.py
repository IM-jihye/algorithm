n,m = map(int,input().split())
card = list(map(int, input().split()))

win = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            add = card[i]+card[j]+card[k]
            if add <= m:
                win.append(add)

print(max(win))