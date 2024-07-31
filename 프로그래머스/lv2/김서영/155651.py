"""
호텔 대실
https://school.programmers.co.kr/learn/courses/30/lessons/155651
"""

def solution(book_time):
    """
    start +1, end -1
    [["10:50", "11:10"], ["10:20", "10:40"], ["10:00", "10:10"]] >> 1
    - key : 퇴실 다음 바로 입실하는 케이스의 경우 +1 먼저 해서 answer(max room) 업데이트하고 -1 하지 않도록 
    1번째 원소 기준으로 또 정렬해줌
    """
    timeline = []
    for start, end in book_time:
        sh, sm = map(int, start.split(':'))
        fh, fm= map(int, end.split(':'))
        timeline.append((sh*60+sm, 1))
        timeline.append((fh*60+fm+10, -1))
    timeline.sort(key=lambda x: (x[0], x[1]))
    
    answer = 0
    room = 0
    for t, x in timeline:
        room += x
        if room > answer: answer = room
    
    return answer