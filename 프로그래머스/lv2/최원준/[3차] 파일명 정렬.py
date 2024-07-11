'''
1. 아이디어 :
    번호가 나올때까지가 Head
    그 뒤 번호가 안나올때까지 number
    나머지 tail
    람다 정렬을 통해서 head 소문자, integer number 오름차순 정렬
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

def solution(files):
    if not files:
        return []
    efiles = []

    for f in files:
        head = ""
        number = ""
        pointer = 0
        while not f[pointer].isdigit():
            head += f[pointer]
            pointer += 1
        while f[pointer].isdigit() and len(number) < 5:
            number += str(f[pointer])
            pointer+=1
        tail = f[pointer:]
        efiles.append((head, number, tail))
    print(efiles)
    efiles.sort(key = lambda x: ( x[0].lower(), int(x[1]) ))
    for i in range(len(efiles)):
        efiles[i] = "".join(efiles[i])
    return efiles


arr = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
arr = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
arr = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2"]
print(solution(arr))