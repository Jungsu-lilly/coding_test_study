# 구현 문제 - left와 right에 해당되는 인덱스를 구한 다음 y와 x중 큰 값의 인덱스+1의 값이다.-> 시간 초과 해결못함

def solution(n, left, right):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    newArr = []
    curr_num = -1
    isPossible = True
    
    for i in range(n):
        if not isPossible:
            break
        for j in range(n):
            arr[i][j] = max(i,j)+1
            arr[j][i] = max(i,j)+1
            curr_num += 1
            if curr_num > right:
                isPossible = False
                break
            if curr_num >= left and curr_num <=right:
                newArr.append(arr[i][j])
    return newArr