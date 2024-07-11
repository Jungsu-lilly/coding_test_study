def dfs(name, money, total, graph):
    global left_money
    left_money = int(money * 0.1)  # 10% 추천인
    total[name] += (money - left_money)  # 90% 가지기

    # 종료 조건 center 하위 노드 or 1원 미만
    if graph[name] == "-" or left_money == 0:
        return
    # 추천인에게 올라가기
    else:
        dfs(graph[name], left_money, total, graph)


def solution(enroll, referral, seller, amount):
    total, graph, answer = {}, {}, []

    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
        total[enroll[i]] = 0

    left_money = 0

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100, total, graph)
    for i in enroll:
        answer.append(total[i])

    return answer