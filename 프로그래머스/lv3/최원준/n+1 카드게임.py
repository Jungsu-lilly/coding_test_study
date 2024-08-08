# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
from itertools import combinations
def solution(coin, cards):

    def get_needs(round, player_cards):
        needs = set()
        target = n + round
        for card in player_cards:
            needs.add(target-card)
        return needs

    n = len(cards)
    num_cards = len(cards)//3
    player_cards = set(cards[:num_cards])
    cards = deque(cards[num_cards:])
    candid_cards = set()
    print(player_cards)
    print(cards)
    ans = 0
    for round in range(1, len(cards)//2 + 1):
        found = False
        target = n + round
        candid_cards.add(cards.popleft())
        candid_cards.add(cards.popleft())
        # 0개
        for player_card in player_cards:
            if target - player_card in player_cards:
                found = True
                player_cards.remove(player_card)
                player_cards.remove(target-player_card)
                break
        # 1개
        if not found and coin >= 1:
            for candid_card in candid_cards:
                if target - candid_card in player_cards:
                    coin -= 1
                    found = True
                    player_cards.remove(target-candid_card)
                    candid_cards.remove(candid_card)
                    break
        # 2개
        if not found and coin >= 2:
            for candid_card in candid_cards:
                if target - candid_card in candid_cards:
                    coin -= 2
                    found = True
                    candid_cards.remove(candid_card)
                    candid_cards.remove(target-candid_card)
                    break

        print(round, coin, candid_cards)
        if not found:
            return round
    return round
