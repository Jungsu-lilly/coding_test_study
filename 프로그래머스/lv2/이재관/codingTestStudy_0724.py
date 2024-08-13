def solution(n):
    answer = []
    answer = [[0 for j in range(1,i+1)] for i in range(1,n+1) ]

    cnt =1
    x=-1
    y=0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1

            elif i % 3 == 1:
                y += 1

            elif i % 3 == 2:
                x -= 1
                y -= 1

            answer[x][y] = cnt
            cnt += 1

    answer = sum(answer,[])
    return answer