from collections import deque

maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
dirs =[
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y+1)
]

def print_r(path):
    curnode=path[-1]
    realpath=[]
    while curnode[2]!=-1:
        realpath.append(curnode[0:2])
        curnode=path[curnode[2]]
    realpath.append(curnode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    queue=deque()
    queue.append((x1,y1,-1))
    maze[x1][y1]=2
    path=[]
    while len(queue)>0:
        curnode=queue.popleft()
        path.append(curnode)
        if curnode[0]==x2 and curnode[2]==y2:
            ## 终点
            print_r(path)
        for dir in dirs:
            nextnode=dir(curnode[0],curnode[1])
            if maze[nextnode[0]][nextnode[1]]==0:
                queue.append((nextnode[0],nextnode[1],len(path)-1))
                ## nextnode一定来自curnode，而curnode一定处在path的最后一个元素
                maze[nextnode[0]][nextnode[1]]==2
                ## 不用break
    else:
        print('没有路')
        return False

print(maze_path_queue(1,1,8,8))