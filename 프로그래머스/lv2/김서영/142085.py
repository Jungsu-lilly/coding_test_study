"""
디펜스게임
https://school.programmers.co.kr/learn/courses/30/lessons/142085

라운드를 하나씩 돌면서 현 시점 필요한 공격력을 더해 -> n 
HeapQ에 넣고
"""
import heapq


def my_solution(n, k, enemy):
    """
    enemy를 돌면서 heapq에 넣고 total로 누적합을 들고있다가
    누적합이 n보다 크게 되면 hq에서 k개만큼 보강해서도 total에 
    도달하지 못하는지 체크하는 방식. 정확도 떨어지고 시간 효율 안남
    """
    if len(enemy) == k:
        return k
    if sum(sorted(enemy, reverse=True)[k:]) <= n: return len(enemy)

    hq = []
    total = 0
    for i, e in enumerate(enemy):
        total += e
        heapq.heappush(hq, -e)
        if total > n and total + sum(hq[:k]) > n:
            return i
    return i+1 if i==len(enemy)-1 else -1


def solution(n, k, enemy):
    """
    while로 돌면서 n+무적권 써도 안되는 경우 리턴하고, 그 전까지는
    - hq에 enemy값 넣고 n에서 빼주기
    - n 0보다 작아지면 무적권으로 보강
    
    while 조건
    """
    if len(enemy) == k: return k

    idx = 0
    hq = []
    while idx < len(enemy):
        e = enemy[idx]
        heapq.heappush(hq, -e) 
        n -= e
        if n<0:
            if k: # 무적권 사용 가능
                # 무적권으로 보강(음수로 저장하고 있으니까 빼주기)
                n -= heapq.heappop(hq) 
                k-=1
            else:
                return idx
        idx += 1
    return idx