/*
https://school.programmers.co.kr/learn/courses/30/lessons/17678

1. 문제분석
배치회수 1~10 n, 간격 1~60 t, 처리개수 1~45 m, 추가로그 00:01~23:59 timetable[] 1~2000개
-> 첫 배치 09:00 -> t분 간격 n회 -> 큐에서 m개씩 처리 -> 정시 추가 건 포함 -> 23:59에 플러시
timetable[]을 미리 알 수 있을 때 -> 추가 가능한 가장 늦은 시간 리턴 (항상 해당시간 맨 뒤에 추가)

2. 풀어보기
n=1,t=1,m=5,timetable=[08:00,08:01,08:02,08:03]
 -> 09:00(5) -> 09:00
n=2,t=10,m=2,timetable=[09:10,09:09,08:00]
 -> 09:00(2),09:10(2) -> 09:09
n=2,t=1,m=2,timetable=[09:00 x 4]
 -> 09:00(2),09:01(2) -> 08:59
n=1,t=1,m=5,timetable=[00:01 x 5]
 -> 09:00(5) -> 00:00
n=1,t=1,m=1,timetable=[23:59]
 -> 09:00(1) -> 09:00
n=10,t=60,m=45,timetable=[23:59 x 16]
 -> 09:00(45),10:00(45),...,18:00(45) -> 18:00
n=2,t=10,m=2,timetable=['09:10','09:09','08:00','09:09']
 -> 09:00(2),09:10(2) -> 09:08

3. 슈도코드
마지막 배치 구하고 -> (9+(n-1)*t/60):((n-1)*t%60)
-> timetable[] 받아서 -> 마지막 배치 이후 값은 일단 제거 -> :로 잘라서 number 연산
-> 나머지 timetable[] 내림차순 정렬하고 -> :로 잘라서 number 연산
첫 배치 부터 m개씩 시간 체크해서 추가 건 count_by_time{}에 담음
 -> 무조건 마지막 배치 -> 최대값의 개수가 m보다 작으면 마지막 시간, 아니면 최대값-1분

4. 구현코드

5. 풀이회고
질문게시판 테스트케이스 추가 해가면서 통과시키긴 했는데, 이렇게 푸는 건 아닐 것 같다
해설 보고 다시 풀어봐야 할 듯
*/
{
  type Time = [number, number];

  const time_asc = (a: Time, b: Time) => a[0] - b[0] || a[1] - b[1];

  const solution = (n: number, t: number, m: number, timetable: string[]) => {
    const last: Time = [9 + Math.trunc(((n - 1) * t) / 60), ((n - 1) * t) % 60];
    const hour_minute: Time[] = timetable
      .map((time) => time.split(":").map((v) => Number(v)) as Time)
      .filter((time) => time_asc(time, last) <= 0)
      .sort(time_asc);
    if (hour_minute.length === 0) {
      return (
        String(last[0]).padStart(2, "0") +
        ":" +
        String(last[1]).padStart(2, "0")
      );
    }

    const count_by_time = new Map<string, number>(); // HH:MM

    let time: Time = [9, 0];
    let index = 0;
    while (time_asc(time, last) <= 0) {
      const key = `${String(time[0]).padStart(2, "0")}:${String(
        time[1]
      ).padStart(2, "0")}`;
      let count = count_by_time.get(key) ?? 0;

      let first = hour_minute[index];
      while (first && time_asc(first, time) <= 0 && count < m) {
        count++;
        first = hour_minute[++index];
      }
      count_by_time.set(key, count);

      time[1] += t;
      if (time[1] >= 60) {
        time[0]++;
        time[1] -= 60;
      }
    }
    while (hour_minute.length - index > 0) {
      hour_minute.pop();
    }

    const count_by_times = Array.from(count_by_time);
    const [_, max_count] = count_by_times[count_by_times.length - 1];
    const max_time = hour_minute[hour_minute.length - 1];
    if (max_count < m) {
      return (
        String(last[0]).padStart(2, "0") +
        ":" +
        String(last[1]).padStart(2, "0")
      );
    } else {
      const [max_hour, max_minute] = max_time;
      if (max_minute === 0) {
        return String(max_hour - 1).padStart(2, "0") + ":59";
      } else {
        return (
          String(max_hour).padStart(2, "0") +
          ":" +
          String(max_minute - 1).padStart(2, "0")
        );
      }
    }
  };

  console.log(solution(3, 1, 2, ["06:00", "23:59", "05:48", "00:01", "00:01"])); // '09:02'
  console.log(solution(2, 10, 2, ["09:10", "09:09", "08:00", "09:09"])); // '09:08'
  console.log(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])); // '09:00'
  console.log(solution(2, 10, 2, ["09:10", "09:09", "08:00"])); // '09:09'
  console.log(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])); // '08:59'
  console.log(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])); // '00:00'
  console.log(solution(1, 1, 1, ["23:59"])); // '09:00'
}
