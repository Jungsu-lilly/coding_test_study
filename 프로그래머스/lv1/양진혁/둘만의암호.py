def solution(s, skip, index):
    skip_set = set(skip)
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip_set]
    alpha_map = {char: idx for idx, char in enumerate(alphabet)}

    return ''.join([alphabet[((alpha_map[i] + index) % len(alphabet))] for i in s])