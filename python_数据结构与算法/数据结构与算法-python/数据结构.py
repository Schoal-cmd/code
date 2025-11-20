#列表
#栈
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        self.stack.pop()
    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack)==0 ##这是一个逻辑运算    ## print(stack.is_empty())    》》True
#栈的应用-括号匹配问题
def brace_match(string):
    match={'}':'{',')':'(',']':'['}
    stack=Stack()
    for i in string:
        if i in {'(','[','{'}:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top()==match[i]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
print(brace_match('(){[()]}[]'))

#队列
#环形队列：front==Maxsize+1时，再前进一个位置自动到0；实现：front=(front+1)%Maxsize(取余)
#队满的条件：(rear+1)%Maxsize==front
class Queue:
    def __init__(self,size=100):
        self.queue=[0 for i in range(size)]
        self.front=0
        self.rear=0
        self.size=size
    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError("Queue is filled.")
    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")
    def is_empty(self):
        return self.front==self.rear
    def is_filled(self):
        return (self.rear+1)%self.size==self.front
q=Queue(5)
for i in range(1,5):
    q.push(i)
print(q.is_filled)
print(q.pop())
q.push(5)
print(q.queue)
#双向队列
#队列内置队列模块
from collections import deque
q=deque([1,2,3],5)
q.append(4) #队尾进队
q.pop() #队尾出队
q.appendleft(5) #队首进队
q.popleft() #队首出队
def tail(n):
    with open('abc.txt','r',encoding='utf-8') as f:
        q=deque(f,n)
        return q 
print(tail(5))

#迷宫问题
#栈——深度优先搜索/回溯法（一条路走到黑，不行就往回走）
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
print(maze)
def maze_path(x1,y1,x2,y2):
    stack=[] #装元组，表示位置
    stack.append((x1,y1)) #起点
    maze[x1][y1]=2
    while(len(stack)>0):
        cursite=stack[-1] #当前位置 元组
        if cursite[0]==x2 and cursite[1]==y2:
            for i in stack:
                print(i)
            return True
            break
        for dir in dirs:
            nextsite=dir(cursite[0],cursite[1])
            if maze[nextsite[0]][nextsite[1]] == 0:
                stack.append(nextsite)
                maze[nextsite[0]][nextsite[1]]=2
                break
        else:
            maze[nextsite[0]][nextsite[1]]=3
            stack.pop()
    else:
        return False
print(maze_path(1,1,8,8))
print(maze)