# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n ** 2 )
3. 자료구조 :
    해시셋
'''


def solution(n, build_frame):
    '''
    x, y =cords
    a = 0 기둥, 1 보
    b = 0 삭제, 1 설치
    기둥은 위쪽 방향 설치
    보는 오른쪽 방향 설치

    '''

    def insert_check(x, y, is_bo):
        if not is_bo: #collar
            bottom_collar = (x, y-1, 0)
            left_bo, right_bo = (x-1, y, 1), (x, y, 1)
            return True if y == 0 or bottom_collar in built_set or left_bo in built_set or right_bo in built_set else False
        elif is_bo: #bo
            left_collar, right_collar = (x, y-1, 0), (x+1, y-1, 0)
            left_bo, right_bo = (x-1, y, 1), (x+1, y, 1)
            return True if left_collar in built_set or right_collar in built_set or (left_bo in built_set and right_bo in built_set) else False

    def remove_check(x, y, is_bo):
        built_set.remove((x, y, is_bo))
        for x2, y2, is_bo2 in list(built_set):
            if not insert_check(x2, y2, is_bo2):
                built_set.add((x, y, is_bo))
                return False
        built_set.add((x, y, is_bo))
        return True

    built_set = set()
    for x, y, is_bo, is_insert in build_frame:
        if is_insert and insert_check(x, y, is_bo):
            built_set.add((x,y,is_bo))
        elif not is_insert and remove_check(x, y, is_bo):
            built_set.remove((x,y,is_bo))

    return sorted(list(built_set))