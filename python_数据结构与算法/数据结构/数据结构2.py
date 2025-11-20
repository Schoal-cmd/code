##链表:数据域、指针;链表的内存可以更灵活的分配；
# 可以利用链表重新实现栈和队列；对图和树结构有很大的启发
##简单手动创建：
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c

print(a.next.next.item)

##链表的创建和遍历访问
##打印链表
def print_linklist(head):
    while head:
        print(head.item,end=',')
        head=head.next
    
###头插法 倒序
def creat_linklist_head(lst):
    head=Node(lst[0])
    for element in lst[1:]:
        note=Node(element)
        note.next=head
        head=note
    return head
head=creat_linklist_head([1,2,3,4])
print(head.next.item)
print_linklist(head)

###尾插法，顺序
def create_linklist_tail(lst):
    head=Node(lst[0])
    tail=head
    for element in lst[1:]:
        note=Node(element)
        tail.next=note
        tail=note
    return head ##输出值还是头
head=create_linklist_tail([1,2,3,4])
print('\n')
print_linklist(head)

##链表的插入和删除：o(1)    列表的插入和删除：o(n)
curnode=b
p=Node(5)
p.next=curnode.next
curnode.next=p
print('\n')
print_linklist(a)

curnode.next=curnode.next.next
del p
print('\n')
print_linklist(a)

##双链表
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prior=None
###双链表插入和删除
p=Node(5)
p.next=curnode.next
curnode.next.prior=p
curnode.next=p
p.prior=curnode
print('\n')
print_linklist(a)

p=curnode.next
curnode.next=p.next
p.next.prior=curnode
del p
print('\n')
print_linklist(a)