##哈希表：通过哈希函数来计算数据存储位置的数据结构=直接寻址表+哈希函数；线性。
###直接寻址表：u大/key小浪费内存；无法处理关键字key不是数字的情况
###哈希函数：除法哈希；乘法哈希；全域哈希
###哈希冲突：1.开放寻址法（线性探查、二次探查、二度探查 换一个哈希函数） 2.拉链法：

class Linklist:
    class Node:
        def __init__(self,item=None):
            self.item=item
            self.next=None
    class Linklistiterator:
        def __init__(self,node):
            self.node=node
        def __next__(self):
            if self.node:
                curnode=self.node
                self.node=curnode.next
                return curnode.item
            else:
                raise StopIteration
        def __iter__(self):
            return self
    def __init__(self,iterable=None):
        self.head=None
        self.tail=None
        if iterable:
            self.extend(iterable)
    def append(self,obj):
        s=Linklist.Node(obj)
        if not self.head:
            self.head=s
            self.tail=s
        else:
            self.tail.next=s
            self.tail=s
    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)
    def find(self,obj):
        for i in self:
            if i==obj:
                return True
            else:
                return False
    def __iter__(self):
        return self.Linklistiterator(self.head)
    def __repr__(self):
        return "<<"+",".join(map(str,self))+">>"

#类似于集合
class Hashtable:
    def __init__(self,size=101):
        self.size=size
        self.T=[Linklist() for i in range(self.size)]
    def h(self,k):
        return k%self.size
    def find(self,k):
        i=self.h(k)
        return self.T[i].find(k)
    def insert(self,k):
        i=self.h(k)
        if self.find(k):
            print('Duplicated Insert.')
        else:
            self.T[i].append(k)

ht=Hashtable()
ht.insert(0)
ht.insert(1)
ht.insert(0)
ht.insert(3)
ht.insert(102)
ht.insert(508)
print(",".join(map(str,ht.T)))
print(ht.find(203))

