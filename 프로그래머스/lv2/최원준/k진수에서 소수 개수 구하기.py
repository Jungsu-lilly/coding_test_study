'''
1. 아이디어 :
    k진수로 변환한다
    "0"을 기준으로 split
    소수인지 확인한다
2. 시간복잡도 :
    O( ?? )
3. 자료구조 :
    배열
'''

def solution(n, k):
    def convert_to_base(n, base):
        if n == 0:
            return "0"
        digits = []
        while n:
            digits.append(int(n % base))
            n = n // base
        return ''.join(str(x) for x in digits[::-1])

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True

    count = 0
    nums = convert_to_base(n, k).split("0")
    for i, n in enumerate(nums):
        count = count + 1 if n != "" and is_prime(int(n)) else count
    return count