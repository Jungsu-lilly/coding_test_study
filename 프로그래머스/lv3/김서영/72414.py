"""
	[(4815, 6314), 
     (1550, 2909), 
     (2431, 3600), 
     (5864, 7350), 
     (5459, 6809)]
    내 start, end 사이에 있는 start 값 찾기
"""

def solution(play_time, adv_time, logs):
    def to_sec(time):
        h, m, s = map(int, time.split(':'))
        return h*3600 + m*60 + s
    
    play_time = to_sec(play_time)
    adv_time = to_sec(adv_time)
    logs = [(to_sec(log.split('-')[0]), to_sec(log.split('-')[1])) for log in logs]
    
    for p1, p2 in logs:
        # 범위 : p1~p1+adv, p2~p2+adv
        # 
    
    return None