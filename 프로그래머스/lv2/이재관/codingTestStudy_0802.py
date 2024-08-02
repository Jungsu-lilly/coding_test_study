def solution(w, h):
    answer = 1
    total = w * h

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    w1 = int(w / gcd(w, h))
    h1 = int(h / gcd(w, h))
    answer = total - (w1 + h1 - 1) * gcd(w, h)

    return answer