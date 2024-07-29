def solution(storey):
    answer = 0
    while storey != 0:
        current = storey % 10
        if current > 5:
            answer += 10 - current
            storey += 10
        elif current < 5:
            answer += current
        else:

        storey //= 10
    return answer
    # answer = 0
    # c = 8
    # while storey > 0:
    #     if storey // (10**c) >= 1:
    #         storey -= 10**c
    #         answer += 1
    #     else:
    #         c -= 1
    # return answer