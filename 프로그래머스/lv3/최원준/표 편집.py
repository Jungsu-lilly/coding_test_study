'''
1. 아이디어 :
    링크드리스트로 풀 수 있다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    LinkedList
'''

class Node:
    def __init__(self, idx):
        self.prev = None
        self.next = None
        self.idx = idx

def solution(n, k, cmd):
    node_arr = [Node(i) for i in range(n)]
    for i in range(1, n):
        node_arr[i - 1].next = node_arr[i]
        node_arr[i].prev = node_arr[i - 1]

    deleted = []
    curr = node_arr[k]
    head = node_arr[0]

    for c in cmd:
        if len(c) == 1:
            if c == "C":
                deleted.append(curr)
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                curr = curr.next if curr.next else curr.prev
            elif c == "Z":
                restored = deleted.pop()
                if restored.prev:
                    restored.prev.next = restored
                else:
                    head = restored
                if restored.next:
                    restored.next.prev = restored
        else:
            dir, val = c.split()
            if dir == "U":
                for _ in range(int(val)):
                    curr = curr.prev
            elif dir == "D":
                for _ in range(int(val)):
                    curr = curr.next

    result = ["X"] * n
    curr = head
    while curr:
        result[curr.idx] = "O"
        curr = curr.next

    return "".join(result)