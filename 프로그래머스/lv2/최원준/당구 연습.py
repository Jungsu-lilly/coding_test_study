# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

def solution(m, n, startX, startY, balls):
    '''
    y1 == y2 and x1 == x2: 0
    y1 == y2 and x1 < x2 : 오른X
    y1 == y2 and x1 > x2 : 왼X
    x1 == x2 and y1 > y2 : 아래X
    x1 == x2 and y1 < y2 : 위X

    오른쪽 = (x1,y1), ( m-x1 + m-x2, abs(y1-y2)   )
    왼쪽 = (x1, y1), ( (x1+x2), abs(y1-y2) )
    아래쪽 = (x1, y1), ( (abs(x1-x2), y1+y2)   )
    위쪽 = (x1, y1), ( (abs(x1-x2), n-y1 + n-y2   )
    '''

    def direction(x1, y1, x2, y2, dir):
        if dir == "right":
            return (m-x1 + m-x2)**2 + (y1-y2)**2
        elif dir == "left":
            return (x1+x2)**2 + (y1-y2)**2
        elif dir == "down":
            return (x1-x2)**2 + (y1+y2)**2
        elif dir == "up":
            return (x1-x2)**2 + (n-y1 + n-y2)**2

    def get_dist(x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return 0
        if y1 == y2 and x1 < x2: #오른 X
            return min(direction(x1,y1,x2,y2,"left"), direction(x1,y1,x2,y2,"down"), direction(x1,y1,x2,y2,"up"))
        if y1 == y2 and x1 > x2: #왼X
            return min(direction(x1,y1,x2,y2,"right"), direction(x1,y1,x2,y2,"down"), direction(x1,y1,x2,y2,"up"))
        if x1 == x2 and y1 > y2: #아래X
            return min(direction(x1,y1,x2,y2,"right"), direction(x1,y1,x2,y2,"left"), direction(x1,y1,x2,y2,"up"))
        if x1 == x2 and y1 < y2: #위X
            return min(direction(x1,y1,x2,y2,"right"), direction(x1,y1,x2,y2,"left"), direction(x1,y1,x2,y2,"down"))
        return min(direction(x1,y1,x2,y2,"left"), direction(x1,y1,x2,y2,"right"), direction(x1,y1,x2,y2,"down"), direction(x1,y1,x2,y2,"up"))

    return [get_dist(startX, startY, x2, y2) for x2, y2 in balls]
