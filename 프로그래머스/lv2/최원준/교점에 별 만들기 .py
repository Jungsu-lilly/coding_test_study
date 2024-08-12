# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(line):
    def get_cross(line1, line2):
        a1, b1, c1 = line1
        a2, b2, c2 = line2
        temp = a1 * b2 - a2 * b1
        if temp == 0:
            return
        x = (b1 * c2 - b2 * c1) / temp
        y = (a2 * c1 - a1 * c2) / temp

        if x.is_integer() and y.is_integer():
            return int(x), int(y)
        return

    points = set()
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            point = get_cross(line[i], line[j])
            if point:
                points.add(point)
    if not points:
        return []

    min_x = min_y = float('inf')
    max_x = max_y = -float('inf')
    for x, y in points:
        min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)

    ans = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in points:
        ans[max_y - y][x - min_x] = '*'

    return [''.join(row) for row in ans]