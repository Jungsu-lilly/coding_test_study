def solution(lines):
    def throughput():
        pass

    def convert(line):
        d, s, t = line.split()
        s = s.split(':')
        t = t.replace('s', '')

        end = (int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])) * 1000
        start = end - float(t) * 1000 + 1
        return ([start, end])

    answer = 0
    log = []
    for line in lines:
        log.append(convert(line))

        answer = max(answer, )

    return answer