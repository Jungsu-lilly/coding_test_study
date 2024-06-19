/*
https://school.programmers.co.kr/learn/courses/30/lessons/87390

1. 문제분석
정수 n, left, right -> n x n 2차원 배열 생성 -> 1행1열~i행1열 i로 채움
 -> 1행, 2행, ..., n행을 이어붙인 1차원 배열 arr 생성
 -> arr[left], arr[left+1], ..., arr[right]만 남기고 나머지 삭제
n는 1~10^7, left와 right는 0~n^2, left~right는 10^5

2. 풀어보기
n=3,left=2,right=5 -> [1,2,3],[2,2,3],[3,3,3] -> [3,2,2,3]
n=4,left=7,right=14 -> [1,2,3,4],[2,2,3,4],[3,3,3,4],[4,4,4,4] -> [4,3,3,3,4,4,4,4]

3. 슈도코드
처음부터 이어서 만들고, 처음부터 잘라서 만든다
첫줄은 1~n, 둘째줄은 2,2~n, 셋째줄은 3,3,3~n, ..., i째줄은 ixi~n
 -> i in 1..n -> j in 1..n -> i와 j중 큰 값 -> i*n+j in left..right
시간초과! -> right-left+1개의 result[]를 만들고 돌려서
 -> i는 index % n, j는 index / n -> index 범위는 left~right

4. 구현코드

5. 풀이회고
경계값 찾는 게 어렵다
*/
const solution = (n: number, left: number, right: number): number[] => {
  return byN(n, left, right);
  // return byNSquare(n, left, right);
};

const byN = (n: number, left: number, right: number): number[] => {
  const result: number[] = [];

  for (let index = left; index <= right; index++) {
    const value = Math.max((index % n) + 1, Math.trunc(index / n) + 1);
    result.push(value);
  }

  return result;
};

const byNSquare = (n: number, left: number, right: number): number[] => {
  const result: number[] = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const index = i * n + j;

      if (index >= left && index <= right) {
        const value = Math.max(i + 1, j + 1);
        result.push(value);

        if (index === right) {
          break;
        }
      }
    }
  }

  return result;
};

console.log(...solution(3, 2, 5)); // [3,2,2,3]
console.log(...solution(4, 7, 14)); // [4,3,3,3,4,4,4,4]
