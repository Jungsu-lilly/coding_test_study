def solution(k, ranges):
    def post_hailstone() -> None:
        lst = [k]
        while 1:
            x=hailstone[-1]
            nx=x // 2 if x % 2==0 else x * 3 + 1
            hailstone.append(nx)
            if nx==1: return
        
            
    def post_integral() -> None:
        for i in range(len(hailstone)-1):
            x1, x2 = min(hailstone[i], hailstone[i+1]), max(hailstone[i], hailstone[i+1])
            integral.append(x1 + (x2-x1)/2)
            
    def get_range_integral(x1, x2) -> int:
        n = len(hailstone)-1
        x2 = n - abs(x2)
        if x1 == x2: return 0.0
        if x1 > x2: return -1.0
        return sum(integral[x1:x2]) * 1.0
    
    answer = []
    hailstone, integral = [k], []
    post_hailstone()
    post_integral()
    for x1, x2 in ranges:
        answer.append(get_range_integral(x1, x2))
    
    return answer