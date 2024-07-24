"""
삼각 달팽이
https://school.programmers.co.kr/learn/courses/30/lessons/68645
"""

def solution(n):
    snail_array = [[1 for _ in range(n)] for _ in range(n)]
    first_idx, val, stop_val = 0, 0, n*(n+1)//2
    while True:
        # print(n, first_idx)
        for i in range(first_idx, n):
            if snail_array[i][first_idx] == 1:
                snail_array[i][first_idx] += val
                val+=1
        # 옆으로
        for i in range(first_idx+1, n):
            if snail_array[n-1][i] == 1:
                snail_array[n-1][i] += val
                val+=1

        # 대각선위로
        for i in range(n-1, first_idx, -1):
            if snail_array[i][i-first_idx] == 1:
                snail_array[i][i-first_idx] += val
                val+=1
        
        first_idx+=1; n-=1
        if val == stop_val:
            break
    
    answer = [1]
    for i in range(1, len(snail_array)):
        for j in range(len(snail_array)):
            if snail_array[i][j] > 1:
                answer.append(snail_array[i][j])

    return answer


solution(4)
# solution(5)
# solution(6)