def solution(numbers):    
    if all(number == 0 for number in numbers): return '0'
    sorted_numbers = sorted(numbers, key=lambda x: str(x) * 10, reverse=True)
    return ''.join(map(str, sorted_numbers))
