'''
1. 아이디어 :
  평균값을 계속 더 하면서, 총합에서 더한 값을 빼고, n도 하나씩 감소시켰습니다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
  배열
'''

def solution(n, s):
    if s//n <= 0:
        return [-1]
    
    arr = []
    temp = n
    while True:
        if len(arr) == n:
            return arr
        arr.append(s//temp)
        s-=s//temp
        temp-=1
    
    return arr
