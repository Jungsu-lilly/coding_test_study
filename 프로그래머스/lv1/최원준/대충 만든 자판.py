# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(keymap, targets):
    def count_press(word):
        press = 0
        for c in word:
            if c not in presses:
                return -1
            press += presses[c]
        return press

    presses = {}
    for button in keymap:
        for i, c in enumerate(button):
            presses[c] = min(presses[c], i+1) if c in presses else i+1
    return [count_press(target) for target in targets]


