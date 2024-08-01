def solution(n):
    answer=[]
    def move(n,sp,tp,dp):
        if n==1:
            answer.append([sp,dp])
        else:
            move(n-1,sp,dp,tp)
            move(1,sp,tp,dp)
            move(n-1,tp,sp,dp)
    move(n,1,2,3)
    return answer