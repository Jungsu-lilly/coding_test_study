/*
https://school.programmers.co.kr/learn/courses/30/lessons/154538

1. 문제분석
자연수 x를 y로 변환 -> x+n, x*2, x*3만 가능
 -> 필요한 최소 연산횟수 리턴 -> 불가능하면 -1
x, y는 1~100만, n은 1~(100만-1)

2. 풀어보기
x=10,y=40,n=5 -> 10*2*2 -> 2
x=10,y=40,n=30 -> 10+30 -> 1
x=2,y=5,n=4 -> 불가 -> -1

3. 슈도코드
연산 x+n, x*2, x*3 정의 -> BFS로 돌리면서, 연산회수 세다가
 -> y와 같아지면 연산회수 리턴 -> 다 넘쳐버리면 -1 리턴

4. 구현코드

5. 풀이회고
DP로 리팩토링
*/
{
const solution = (x: number, y: number, n: number): number => {
  if (x === y) {
    return 0;
  }

  return by_bfs(x, y, n);
};

const by_bfs = (x: number, y: number, n: number) => {
  const queue: [number, number][] = [[x, 0]];
  let first = 0;

  while (first < queue.length) {
    const [sum, count] = queue[first++];
    if (sum === y) {
      return count;
    }

    if (sum < y) {
      queue.push([sum + n, count + 1]);
      queue.push([sum * 2, count + 1]);
      queue.push([sum * 3, count + 1]);
    }
  }

  return -1;
};

console.log(solution(10, 40, 5)); // 2
console.log(solution(10, 40, 30)); // 1
console.log(solution(2, 5, 4)); // -1
}
