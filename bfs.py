from collections import deque


def bfs(graph,start):


    visited=set()
    queue=deque()
    predecessor={}



    visited.add(start)
    queue.append(start)
    predecessor[start]=None



    while queue:
        current=queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:

                visited.add(neighbor)
                predecessor[neighbor]=current
                queue.append(neighbor)
    
    return visited  # если вернуть  predecessor он древо путей даст(кто  от кого пришел)



graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A'],
    'D':['B']
}


result=bfs(graph,'A')

print(result)