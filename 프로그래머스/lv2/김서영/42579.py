"""
베스트앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""

def solution(genres, plays):
    from collections import defaultdict
    
    # 0 : 각 장르 누적 플레이 수, [] : (play, idx)를 원소로 갖는 리스트
    dix = defaultdict(lambda: [0, []]) 
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        dix[genre][0] += play
        dix[genre][1].append((play, i))
    # 장르 누적합 기준으로 먼저 정렬
    dix_v = list(dix.values()).sort(key=lambda x: x[0], reverse=True)
    # 각 장르에서 상위 최대 2개 뽑기
    answer = []
    for _, play_lst in dix_v:
        play_lst.sort(key=lambda x: x[0], reverse=True)
        answer += [p[1] for p in play_lst][:2]
        
    return answer