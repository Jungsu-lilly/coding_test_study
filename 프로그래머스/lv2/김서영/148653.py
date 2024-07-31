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
        if num in visited: return visited[num]
        # 한자리수인경우 0-5는 num, 6-9는 각각 5,4,3,2 리턴해야함
        if len(num) == 1: 
            if num in [6,7,8,9]: return 11-int(num)+stone
            return int(num)+stone

        multiply = 10**(len(num)-1)
        lower = int(num[0])
        upper = int(num[0])+1

        ans = min(
            backtrack(str(int(num) - lower*multiply), stone+lower),
            backtrack(str(upper*multiply - int(num)), stone+upper)
        )

        visited[num] = ans
        return ans
    
    visited = {}
    answer = backtrack(str(storey), 0)
    print(answer)
    return answer

solution(16)
solution(2554)