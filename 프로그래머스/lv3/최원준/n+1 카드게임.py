from collections import deque

def solution(coin, cards):
    n = len(cards)
    num_cards = n // 3
    player_cards = set(cards[:num_cards])
    cards = deque(cards[num_cards:])
    candid_cards = set()

    round = 1
    while cards:
        if len(cards) < 2:
            break

        target = n + 1
        found = False


        candid_cards.add(cards.popleft())
        candid_cards.add(cards.popleft())

        # 0개
        for card in player_cards:
            if target - card in player_cards and card != target - card:
                player_cards.remove(card)
                player_cards.remove(target - card)
                found = True
                break

        # 1개
        if not found and coin >= 1:
            for candid_card in list(candid_cards):
                if target - candid_card in player_cards:
                    coin -= 1
                    found = True
                    player_cards.remove(target - candid_card)
                    player_cards.add(candid_card)
                    candid_cards.remove(candid_card)
                    break

        # 2개
        if not found and coin >= 2:
            for candid_card in list(candid_cards):
                if target - candid_card in candid_cards:
                    coin -= 2
                    found = True
                    candid_cards.remove(candid_card)
                    candid_cards.remove(target - candid_card)
                    break

        # print(round, coin, candid_cards)
        if not found:
            return round
        round += 1

    return round

