def solution(book_time):
    answer = 0

    first_b = 1500
    last_b = 0

    for i in range(len(book_time)):
        start_h, start_m = list(map(int, book_time[i][0].split(':')))
        end_h, end_m = list(map(int, book_time[i][1].split(':')))

        start_time = start_h * 60 + start_m
        end_time = end_h * 60 + end_m

        book_time[i][0] = start_time
        book_time[i][1] = end_time

        if first_b > start_time:
            first_b = start_time

        if end_time > last_b:
            last_b = end_time

    total_book = [0] * (last_b - first_b)

    for j in range(len(book_time)):
        tmp_s = book_time[j][0] - first_b
        tmp_e = book_time[j][1] - first_b
        tmp_book = [1] * (tmp_e - tmp_s)

        total_book[tmp_s:tmp_e + 1] = [a + b for a, b in zip(total_book[tmp_s:tmp_e + 1], tmp_book)]

    answer = max(total_book)

    return answer