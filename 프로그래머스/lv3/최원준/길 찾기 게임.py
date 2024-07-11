'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys
sys.setrecursionlimit(10000)
def solution(nodeinfo):
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))
    print(nodes)
    pre_order = []
    post_order = []

    def dfs(nodes):
        if not nodes:
            return None

        root = nodes[0]
        left_subtree = [node for node in nodes if node[0] < root[0]]
        right_subtree = [node for node in nodes if node[0] > root[0]]

        pre_order.append(root[2])  # 전위 순회: 루트 방문
        dfs(left_subtree)          # 왼쪽 서브트리 방문
        dfs(right_subtree)         # 오른쪽 서브트리 방문
        post_order.append(root[2]) # 후위 순회: 루트 방문

        return root

    dfs(nodes)

    return [pre_order, post_order]