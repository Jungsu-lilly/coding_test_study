"""
로또의 최고 순위와 최저 순위
https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""

def solution(lottos, win_nums):
    import bisect
    
    lottos.sort()
    win_nums.sort()
    numof_zero, numof_correct = 0, 0
    for l in lottos:
        if l == 0:
            numof_zero+=1
            continue
        idx = bisect.bisect(win_nums, l) # 같은 원소 있을 시 그 다음 위치 받음
        if win_nums[idx-1] == l: 
            numof_correct+=1
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    return [rank[numof_correct+numof_zero], rank[numof_correct]]