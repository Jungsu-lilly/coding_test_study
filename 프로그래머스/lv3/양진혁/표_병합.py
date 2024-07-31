def solution(commands):
    table = [['' for _ in range(51)] for _ in range(51)]
    answer = []

    def update1(r, c, value):
        table[r][c] = value

    def update2(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j] == value1:
                    table[i][j] = value2

    def merge(r1, c1, r2, c2):
        pass

    def unmerge(r, c):
        pass

    def print_cell(r, c):
        answer.append(table[r][c]) if table[r][c] != '' else "EMPTY"

    for command in commands:
        cmd, *arg = command.split()
        if command[0] == "UPDATE":
            if len(arg) == 3:
                update1(int(arg[0]), int(arg[1]), arg[2])
            else:
                update2(arg[0], arg[1])

        elif commands[0] == "MERGE":
            r1, c1, r2, c2 = map(int, arg)
            merge(r1, c1, r2, c2)

        elif commands[0] == "UNMERGE":
            r, c = map(int, arg)
            unmerge(r, c)

        else:
            r, c = map(int, arg)
            print_cell(r, c)

    return answer



