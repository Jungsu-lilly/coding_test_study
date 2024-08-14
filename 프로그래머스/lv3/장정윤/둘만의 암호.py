def solution(s, skip, index):
    answer = ''
    for char in s:
        cnt = 0
        curr_char = char
        
        while cnt < index:
            curr_char = chr(ord(curr_char)+1)
            if curr_char > 'z':
                curr_char = chr(ord(curr_char) - 26)
            if curr_char not in skip:
                cnt += 1
        answer += curr_char   
    return answer