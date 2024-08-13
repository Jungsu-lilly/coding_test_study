def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열로 정렬하면 맨 앞 부터 비교 -> 3배 곱해줘서 뒤에 까지 정렬해주기
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))

    return answer