'''
1. 아이디어 :
    점화식 노가다..
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    -
'''

def solution(n, left, right):
    ans = []
    for i in range(left, right+1):
        ans.append(max( (i//n)+1 , (i%n)+1 ))
    return ans