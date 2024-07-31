def solution(n):
    def hanoi(fr, mid, to, n):
        if n == 1: 
            answer.append([fr, to])
            return
        # n-1개 원판 mid로 옮기기
        hanoi(fr, to, mid, n-1)
        # 가장 큰 원판 to로 옮기기
        answer.append([fr, to])
        # n-1개 원판 to로 옮기기
        hanoi(mid, fr, to, n-1)
    answer = []
    hanoi(1, 2, 3, n)
    return answer