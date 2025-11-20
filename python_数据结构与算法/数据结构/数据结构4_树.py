
#树的实例：模拟文件系统
##节点定义
class Node:
    def __init__(self,name,type='dir'):
        self.name=name
        self.type=type
        self.children=[]
        self.parent=None
        ###链式储存
    def __repr__(self): ###显示触发，只要有打印行为需要字符串就会自动触发
        return self.name
    
n=Node("hello")
n2=Node("world")
n.children.append(n2)
n2.parent=n

class Filesystemtree:
    def __init__(self):
        self.root=Node('/')
        self.now=self.root
    def mkdir(self,name):
        if name[-1]!='/':
            name+='/'
        n=Node(name)
        self.now.children.append(n)
        n.parent=self.now
    def ls(self):
        return self.now.children
    def cd(self,name):
        if name[-1]!='/':
            name+='/'
        if name=='../':
            self.now=self.now.parent
            return
        for child in self.now.children:
            if child.name==name:
                self.now=child
                return
        raise ValueError("invalid dir")

        
tree=Filesystemtree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')

tree.cd('bin/')
tree.mkdir('python/')

tree.cd('../')
print(tree.ls())

#二叉树的遍历
##节点定义
class Bitreenode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

a=Bitreenode('A')
b=Bitreenode('B')
c=Bitreenode('C')
d=Bitreenode('D')
e=Bitreenode('E')
f=Bitreenode('F')
g=Bitreenode('G')
e.lchild=a
e.rchild=g
a.rchild=c
c.lchild=b
c.rchild=d
g.rchild=f

##前序遍历
def pre_order(root):
    if root:
        print(root.data,end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)
pre_order(e)
print('\n')
##中序遍历
def im_order(root):
    if root:
        im_order(root.lchild)
        print(root.data,end=',')
        im_order(root.rchild)
im_order(e)
print('\n')
##后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')
post_order(e)
print('\n')
##层次遍历-用队列
from collections import deque
def level_order(root):
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
level_order(e)
print('\n')