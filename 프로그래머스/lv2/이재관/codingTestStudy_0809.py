def solution(k, ranges)
    def getExtent(x,y):
        extent = (x+y)*1/2
        return extent


    ubak = [k]
    while k>1:
        if k%2==0:
            k=k/2
            ubak.append(k)
        elif k%2==1:
            k=(k*3)+1
            ubak.append(k)



    answer = []
    for i in range(len(ranges)):
        result = 0
        a,b = ranges[i]

        if (a, b) == (0, 0):
            for j in range(len(ubak) - 1):
                result += getExtent(ubak[j], ubak[j + 1])
            answer.append(result)
            print(a,b)

        else:
            b = len(ubak)-1 + b

            if a>b:
                answer.append(-1.0)
            else:
                print(a,b)
                for j in range(a, b):
                    result += getExtent(ubak[j], ubak[j + 1])
                answer.append(result)