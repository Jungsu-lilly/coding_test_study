'''
1. 아이디어 :
    투 포인터로 풀 수 있다.
    kinds = 보석의 종류 갯수
    dict = 보석의 종류 갯수 추적
    dict와 kinds 길이가 같을떄까지 right를 옮겨주고,
    같다면 left를 옮겨주면서 값 갱신
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''


def solution(gems):
    kinds = len(set(gems))

    cmax = len(gems)
    ans = [0,0]
    left = 0
    right = 0

    dict = {}
    while right < len(gems):
        if gems[right] not in dict:
            dict[gems[right]] = 0
        dict[gems[right]] += 1
        right += 1

        while len(dict) == kinds:
            if right-left-1 < cmax:
                cmax = right-left-1
                ans = [left+1, right]

            if dict[gems[left]] == 1:
                del dict[gems[left]]
            else:
                dict[gems[left]] -= 1
            left += 1

    if right-left < cmax:
        ans = [left+1, right]

    return ans


arr = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# arr = ["AA", "AB", "AC", "AA", "AC"]
arr = ["XYZ", "XYZ", "XYZ"]
arr = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
arr = ["DIA", "SAPPHIRE", "SAPPHIRE", "DIA"]
print(solution(arr))
