"""
마법의 엘리베이터
https://school.programmers.co.kr/learn/courses/30/lessons/148653

16 = 10+6 -> 7
   = 20-4 -> 6

2554 = 2000+500+50+4 -> 16
     = 3000-400-50-4 -> 16 -> 3000-2554 = 4463s

     
2539 = 2000+500+30+9
     = 2000+500-40+1
"""

def solution(storey):
    
    def backtrack(num: str, stone: int):
        """
                      (2554,0)
            (554,2)             (546,3)
        (54,2+5)  (46,2+6)      (46,3+5)  (54,3+6)
        """
        nonlocal answer
        # if (num, stone) in visited: return
        if len(num) == 1:
            answer = min(answer, stone+int(num))
            return answer
        # visited.add((num, stone))
        multiply = 10**(len(num)-1)
        lower = int(num[0])
        upper = int(num[0])+1
        
        return min(
            backtrack(str(int(num) - lower*multiply), stone+lower),
            backtrack(str(upper*multiply - int(num)), stone+upper)
        )

    answer = 1e10
    backtrack(str(storey), 0)
    
    return answer

solution(16)
solution(2554)