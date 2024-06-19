/*
https://school.programmers.co.kr/learn/courses/30/lessons/12938

1. 문제분석
자연수 n개 [] -> 합이 s이고, 곱이 최대인 케이스 리턴
-> 오름차순 정렬, 불가능하면 [-1], n은 자연수 1~1만, s는 자연수 1~1억

2. 풀어보기
n=2,s=9 -> [1,8],[2,7],[3,6],[4,5] -> 8,14,18,20 -> [4,5]
n=2,s=1 -> [-1]
n=2,s=8 -> [1,7],[2,6],[3,5],[4,4] -> 7,12,15,16 -> [4,4]
n=3,s=9 -> [1,1,7],[1,2,6],[1,3,5],[1,4,4],[2,1,6],[2,2,5],[2,3,4],[3,1,5],[3,2,4],[3,3,3]
 -> 7,12,15,16,12,20,24,15,24,27

3. 슈도코드
s를 n으로 나누고 -> Math.trunc 후 s에서 빼서 push -> 반복

4. 구현코드

5. 풀이회고
엄청 간단한 문제
*/
const solution = (n: number, s: number): number[] => {
  if (n === s) {
    return Array.from({ length: n }, (v, i) => 1);
  }

  const result: number[] = [];

  let number = Math.trunc(s / n);
  while (number > 0) {
    result.push(number);
    s = s - number;
    n = n - 1;
    number = Math.trunc(s / n);
  }

  return result.length ? result : [-1];
};

console.log(solution(2, 9)); // [4, 5]
console.log(solution(2, 1)); // [-1]
console.log(solution(2, 8)); // [4, 4]
