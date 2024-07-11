#

'''
1. 아이디어 :
    n 진법으로 변환 + for loop
2. 시간복잡도 :
    k log(n) k (k = max_length)
3. 자료구조 :
    배열
'''


def solution(n, t, m, p):
    def convert(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = []
        while num:
            result.append(digits[num % base])  # num을 base로 나눈 나머지부터 채운다.
            num = n // base
        return ''.join(result[::-1])

    max_length = (t * m) - (m - p)
    # (숫자 * 인원) - (마지막 사이클의 내 차례의 번호 - 해당 사이클의 나머지 인원)
    # 011011100 -> 0110111
    s = ""
    num = 0
    while len(s) < max_length:
        s += convert(num, n)
        num += 1

    return "".join([s[i] for i in range(p - 1, max_length, m)])
