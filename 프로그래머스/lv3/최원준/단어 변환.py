# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    bfs의 개념으로 풀 수 있습니다.
2. 시간복잡도 :
    O( n * k )
3. 자료구조 :
    배열
'''

def solution(begin, target, words):
    def find_candid(curr_word):
        size = len(curr_word)
        candid = []
        for word in words:
            if word in visited:
                continue
            difference = 0
            for i in range(size):
                if word[i] != curr_word[i]:
                    difference += 1
                if difference > 1:
                    break
            if difference <= 1:
                candid.append(word)
                visited.add(word)
        return candid

    if target not in words:
        return 0

    visited = set()
    converts = 0
    start = [begin]

    for i in range(len(words)):
        temp = []
        while start:
            curr_word = start.pop()
            if curr_word == target:
                return converts
            temp += find_candid(curr_word)
        converts += 1
        start = temp[:]

    return 0
