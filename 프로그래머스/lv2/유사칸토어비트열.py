def solution(n, l, r):
    cantor = '1'

    for _ in range(1, n + 1):
        temp = ''
        for char in cantor:
            if char == '1':
                temp += '11011'
            else:
                temp += '00000'
        cantor = temp

    return list(map(int, cantor[l - 1:r])).count(1)
