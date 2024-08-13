def solution(line):
    answer = []

    def cross_p(p1, p2):
        a, b, e = p1
        c, d, f = p2

        if (a * d) - (b * c) == 0:
            return False

        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)

        return [x, y]

    cross_points = []
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            cross_points.append(cross_p(line[i], line[j]))

    cross_points = list(filter(None, cross_points))
    filtered_points = []
    left = float('inf')
    right = float('-inf')
    top = float('-inf')
    bottom = float('inf')

    for i in cross_points:
        if i == list(map(int, i)):
            filtered_points.append(list(map(int, i)))

            if i[0] < left:
                left = i[0]
            if i[0] > right:
                right = i[0]
            if i[1] > top:
                top = i[1]
            if i[1] < bottom:
                bottom = i[1]

    width = int(right - left) + 1
    height = int(top - bottom) + 1

    for i in range(height):
        answer.append(['.'] * width)

    filtered_points = sorted(filtered_points, key=lambda x: x[1], reverse=True)
    filtered_points
    for i in filtered_points:
        x, y = int(abs(top)) - i[1], int(abs(left)) - i[0]
        answer[x][y] = '*'

    answer = [''.join(height) for height in answer]

    return answer