"""
태이블 해사 험수
https://school.programmers.co.kr/learn/courses/30/lessons/147354
"""

def solution(data, col, row_begin, row_end):
    
    answer = 0
    # {data내에서의 인덱스: i값}
    # (col번째 값, 해당 값 인덱스) 를 원소로 갖는 리스트
    col_st_elements = [[e, i] for i, e in enumerate(list(zip(*data))[col-1])]
    # col번째 값 기준으로 정렬
    col_st_elements.sort(key=lambda x: x[0])
    # rank 계산
    prev, prev_rank = -1, 0
    for i in range(len(data)):
        if col_st_elements[i][0] != prev:
            col_st_elements[i].append(i+1)
            prev, prev_rank = col_st_elements[i][0], i+1
        else:
            col_st_elements[i].append(prev_rank)

    return answer
