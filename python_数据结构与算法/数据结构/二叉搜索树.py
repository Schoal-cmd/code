import random
#二叉搜索树：节点的左孩子节点都比他小，右孩子节点都比他大
#相当于二分查找；最多查找树的深度次
class Bitreenode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

class BST:
    def __init__(self,li=None):
        self.root=None
        if li:
            for val in li:
                self.insert_no_rec(val)
    ##插入
    ###用递归
    def insert(self,node,val):
        if not node:
            node=Bitreenode(val)
        elif val<node.data:
            node.lchild=self.insert(node.lchild,val)
            node.lchild.parent=node
        elif val>node.data:
            node.rchild=self.insert(node.rchild,val)
            node.rchild.parent=node
        return node
    ###不递归
    def insert_no_rec(self,val):
        p=self.root
        if not p:
            self.root=Bitreenode(val)
            return
        while True:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=Bitreenode(val)
                    p.lchild.parent=p
                    return
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=Bitreenode(val)
                    p.rchild.parent=p
                    return
            else:
                return
    ##查询
    def query(self,node,val):
        if not node:
            return None
        elif val<node.data:
            return self.query(node.lchild,val)
        elif val>node.data:
            return self.query(node.rchild,val)
        else:
            return node
    
    def query_no_rec(self,val):
        p=self.root
        while p:
            if val<p.data:
                p=p.lchild
            elif val>p.data:
                p=p.rchild
            else:
                return p
        return None


    def pre_order(self,root):
        if root:
            print(root.data,end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)


    def im_order(self,root):
        if root:
            self.im_order(root.lchild)
            print(root.data,end=',')
            self.im_order(root.rchild)


    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=',')
    ##删除
    def remove_1(self,node):###情况1：node是叶子节点
        if not node.parent:
            self.root=None
        elif node==node.parent.lchild:
            node.parent.lchild=None
            node.parent=None
        elif node==node.parent.rchild:
            node.parent.rchild=None
            node.parent=None

    def remove_21(self,node): ###情况2：node只有一个左孩子
        if not node.parent:
            self.root=node.lchild
            node.lchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
        elif node==node.parent.rchild:
            node.parent.rchild=node.lchild
            node.lchild.parent=node.parent

    def remove_22(self,node): ###情况2：node只有一个右孩子
        if not node.parent:
            self.root=node.rchild
            node.rchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.rchild
            node.rchild.parent=node.parent
        elif node==node.parent.rchild:
            node.parent.rchild=node.rchild
            node.rchild.parent=node.parent

    def delete(self,val):
        if self.root: ###不是空树
            node=self.query_no_rec(val)
            if not node: ###不存在
                return False
            elif not node.lchild and not node.rchild:
                self.remove_1(node)
            elif node.lchild and not node.rchild:
                self.remove_21(node)
            elif not node.lchild and node.rchild:
                self.remove_22
            else: ###两个孩子都有
                min_node=node.rchild
                while min_node.lchild:
                    min_node=min_node.lchild
                node.data=min_node.data
                ####删除min_node
                if min_node.rchild:
                    self.remove_22(min_node)
                else:
                    self.remove_1(min_node)

li=list(range(0,500,2))
random.shuffle(li)
lst=[1,2,3,4,5,6,7,8,9]

tree=BST(lst)
tree.pre_order(tree.root)
print("")
tree.im_order(tree.root) ##中序序列是升序
print("")
tree.post_order(tree.root)

treee=BST(li)
print("")
print(tree.query_no_rec(4).data)

tree.delete(6)
tree.pre_order(tree.root)












































