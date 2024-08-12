def solution(genres, plays):
    answer = []
    dic = {}
    
    # 장르별로 노래 재생 횟수 저장
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i], i))
        else:
            dic[genres[i]] = [(plays[i], i)]
            
    # 장르별 재생 횟수의 총합으로 장르 정렬
    sorted_genres = sorted(dic.keys(), key=lambda g: sum(play for play, _ in dic[g]), reverse=True)
    
    # 정렬된 장르 순서대로
    for genre in sorted_genres:
        # 장르 내 노래들을 재생 횟수로 정렬, 재생 횟수 같으면 고유 번호로 정렬
        sorted_plays = sorted(dic[genre], key=lambda x: (-x[0], x[1]))
        # 최대 2곡 선택
        for play in sorted_plays[:2]:
            answer.append(play[1])  # 고유 번호 추가
    
    return answer