'''
1. 아이디어 :
    각각의 gcd(최대 공약수)를 구하고, 해당 gcd가 다른 배열의 모든 원소들에 대해 나눠질수 있는지 확인
    gcd가 2 이상이고 나눠질 수 없다면 정답이 될 수 있다.
2. 시간복잡도 :
    O( nlog max(A) + mlog max(B) )
3. 자료구조 :
    -
'''

def solution(arrayA, arrayB):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def get_gcd(array):
        ans = array[0]
        for num in array[1:]:
            ans = gcd(ans, num)
        return ans

    def divisible(g, array):
        for n in array:
            if n % g == 0:
                return True
        return False

    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)

    validA = gcdA != 1 and not divisible(gcdA, arrayB)
    validB = gcdB != 1 and not divisible(gcdB, arrayA)

    return max(gcdA if validA else 0, gcdB if validB else 0)
