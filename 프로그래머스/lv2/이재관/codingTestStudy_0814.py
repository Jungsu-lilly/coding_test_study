def solution(s, skip, index):
    answer =''
    ord_skip = [ord(char) for char in skip]

    answer = ''
    for i in s:
        tmp_s = ord(i)
        cnt = 0

        while cnt < index:
            tmp_s += 1
            if tmp_s > ord('z'):
                tmp_s = ord('a')
            if tmp_s not in ord_skip:
                cnt += 1

        answer += chr(tmp_s)
    return answer