tree= {
    '1': [],
    '2': [],
    '3': ['5','8','25'],
    '4': [],
    '5': ['1','2'],
    '6': ['4','9'],
    '8': [],
    '9': [],
    '12': ['6'],
    '25': ['8','12']
}

queue=[]
visited=[]

def bfs(visited,tree,node):
    visited.append(node)
    queue.append(node)

    print("bfs: ")
    while queue:
        p=queue.pop(0)
        print(p,end=" ")
        for adjacent_node in tree[p]:
            if adjacent_node not in visited:
                visited.append(adjacent_node)
                queue.append(adjacent_node)

bfs(visited,tree,'3')

stack=[]
visited=[]
print("\ndfs: ")
def dfs(visited,tree,node):
    i=0
    visited.append(node)
    stack.append(node)

    while stack:
        s=stack.pop(i)
        i=i-1
        print(s,end=" ")

        for adjacent in tree[s]:
            if adjacent not in visited:
                visited.append(adjacent)
                stack.append(adjacent)
                i+=1

dfs(visited,tree,'3')