t = int(input())

for i in range(t):
    quiz = list(input())
    score = 0
    score_list = 0

    for j in quiz:
        if j in 'O':
           score += 1
           score_list += score
        else:
            score =0

    print(score_list)