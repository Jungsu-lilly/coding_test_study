'''
1. 아이디어 :
    시작점과 도착점을 정렬 후에 set에 넣는다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    해시셋
'''

def solution(dirs):
    def get_path(x1, y1, x2, y2):
        a = sorted([[x1,y1], [x2,y2]], key= lambda x: (x[0], x[1]))
        return (a[0][0], a[0][1], a[1][0], a[1][1])

    visited = set()
    dict = {"L":[-1,0], "D":[0,-1], "U":[0,1], "R":[1,0]}

    curr = [0,0]
    for dir in dirs:
        x, y = dict[dir]
        if not (-5 <= curr[0]+x <= 5 and -5 <= curr[1] + y <= 5):
            continue
        visited.add(get_path(curr[0], curr[1], curr[0]+x, curr[1]+y))
        curr[0] += x
        curr[1] += y
    return len(visited)
