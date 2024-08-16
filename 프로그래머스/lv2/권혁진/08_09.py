# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    ks = [k]
    while k != 1:
        if k % 2 == 0: k //= 2
        else: k = 3*k + 1
        ks.append(k)
    results = []
    for i in ranges:
        start = i[0]
        end = len(ks) - 1 + i[1]
        if start > end: 
            results.append(-1.0)
        else:
            average = 0
            for j in range(start, end):
                average += (ks[j] + ks[j+1]) / 2
            results.append(float(average))
    return results