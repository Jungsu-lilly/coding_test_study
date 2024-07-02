def solution(m, musicinfos):
    answer = ''
    mx = 0
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        st, et, name, info = musicinfo
        st = int(st[:2] * 60) + int(st[3:])
        et = int(et[:2] * 60) + int(et[3:])

        tmp = ''
        div, mod = divmod(et - st, len(info))
        tmp = info * div + info[:mod]

        for i in range(len(tmp)):
            if tmp[i:i + len(m)] == m and tmp[i + len(m)] != '#':
                if mx < et - st:
                    mx = max(mx, et - st)
                    answer = name
    if answer != '':
        return answer
    else:
        return None