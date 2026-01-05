from collections import defaultdict,deque
graph = defaultdict(list)

edges=[(0,1),(0,2),(1,3),(2,3)]

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def bfs(start):
    visited=set()
    queue=deque([start])
    visited.add(start)

    while queue:
        node=queue.popleft()
        print(node,end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(0)