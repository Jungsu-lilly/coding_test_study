def solution(storey):
    answer = 0

    storey_split = [int(i) for i in str(storey)]
    storey_split.reverse()
    storey_split.append(0)

    for i in range(len(storey_split)):
        if (storey_split[i] > 5):
            answer += 10 - storey_split[i]
            storey_split[i + 1] += 1

        elif (storey_split[i] == 5):
            if (storey_split[i + 1] < 5):
                answer += storey_split[i]
            else:
                answer += 10 - storey_split[i]
                storey_split[i + 1] += 1

        else:
            answer += storey_split[i]

    return answer