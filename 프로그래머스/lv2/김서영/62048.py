def gcd_eucli(a, b):
    if b==0: 
        print(f"return gcd {a}")
        return a
    else: return gcd_eucli(b, a % b)


def solution(w, h):
    print(w, h)
    gcd = gcd_eucli(w, h)
    cut = (w / gcd + h / gcd - 1) * gcd
    print(w * h - cut)
    return w * h - cut


solution(8, 12)
solution(8, 15)
solution(6, 9) 
