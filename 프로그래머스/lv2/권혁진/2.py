# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def intersection_point(a, b, e, c, d, f):
    if a*d - b*c == 0: return None
    x = (b*f - e*d)/(a*d - b*c)
    y = (e*c - a*f)/(a*d - b*c)
    if x == x//1 and y == y//1:
        return [int(x), int(y)]
    return None

def solution(line):
    points = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            point = intersection_point(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2])
            if point: points.append(point)

    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    answer = []
    for i in range(max_y, min_y-1, -1):
        row = ''
        for j in range(min_x, max_x+1):
            check = False
            for point in points:
                if [j, i] == point:
                    row += '*'
                    check = True
                    break
            if not check: row += '.'
        answer.append(row)
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))