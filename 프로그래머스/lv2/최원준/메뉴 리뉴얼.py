'''
1. 아이디어 :
    백트래킹으로 각 손님들이 시킨 메뉴들의 조합들을 구하고, 조합들을 카운트한다
    단품메뉴들의 갯수(course)와 조합의 길이를 비교하여, 가장 많이 등장한 조합들을 저장하고 정렬한다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    해시맵
'''

from collections import defaultdict
def solution(orders, course):
    courses = defaultdict(int)
    for i in range(len(orders)):
        orders[i] = list(orders[i])

    def backtrack(s, idx, menu_list):
        if len(s) >= 2:
            courses["".join(sorted(s))] += 1

        for i in range(idx+1, len(menu_list)):
            backtrack(s+menu_list[i], i, menu_list)

    for i in range(len(orders)):
        backtrack("", -1, orders[i])

    courses = {k : v for k, v in courses.items() if v >= 2}

    ans = []
    for menu_count in course:
        temp = []
        cmax = 0
        for k, v in courses.items():
            if len(k) != menu_count:
                continue
            if v > cmax:
                cmax = v
                temp = [k]
            elif v == cmax:
                temp.append(k)
        for c in temp:
            ans.append(c)

    return sorted(ans)