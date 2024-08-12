# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
def solution(genres, plays):
    songs = defaultdict(list)
    play_count = defaultdict(int)

    for i in range(len(genres)):
        play_count[genres[i]] += plays[i]
        songs[genres[i]].append((plays[i], i))

    play_count = sorted([[v,k] for k, v in play_count.items()], reverse=True)

    ans = []
    for play, genre in play_count:
        song_list = sorted(songs[genre], key = lambda x: (-x[0], x[1]))[:2]
        for i in range(max(1, len(song_list))):
            ans.append(song_list[i][1])

    return ans