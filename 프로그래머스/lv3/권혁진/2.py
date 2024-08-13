# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    dict = {}
    specific_dict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in dict:
            dict[genre] = play
            specific_dict[genre] = [(play, i)]
        else:
            dict[genre] += play
            specific_dict[genre].append((play, i))

    sorted_genres = sorted(dict.keys(), key=lambda x: dict[x], reverse=True)
    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(specific_dict[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))