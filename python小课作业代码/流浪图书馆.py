class Book:
    def __init__(self,name,author,comment,state=0):
        #0代表未借出，1代表已借出
        self.name=name
        self.author=author
        self.comment=comment
        self.state=state

    def __str__(self):
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》\n作者：%s\n推荐语：%s\n借阅状态：%s'%(self.name,self.author,self.comment,status)

class BookManager:
    books=[]
    authors = []
    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        book4 = Book('撒哈拉的故事','三毛','我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book5 = Book('梦里花落知多少','三毛','人人都曾拥有荷西，虽然他终会离去。')
        book6 = Book('月亮与六便士','毛姆','满地都是六便士，他却抬头看见了月亮。')
        self.books.extend([book1,book2,book3,book4,book5,book6])
        self.authors.extend([book1.author,book2.author,book3.author,book4.author,book5.author,book6.author])
    
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.查询作者\n6.退出系统\n')
            choice=int(input('请输入数字选择对应的功能：'))
            if choice==1:
                self.show_all_book()
            elif choice==2:
                self.add_book()
            elif choice==3:
                self.lend_book()
            elif choice==4:
                self.return_book()
            elif choice==5:
                self.show_author_book()
            elif choice==6:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
            break

    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        new_name=input('请输入书籍名称：')
        new_author=input('请输入书籍作者：')
        new_comment=input('请输入书籍推荐语：')
        new_book=Book(new_name,new_author,new_comment)
        self.books.append(new_book)
        print('书籍添加成功，信息如下：')
        print(new_book)
        print('感谢您的善举，愿书籍的岛屿能因你我的托举而永世伫立。')
    
    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def lend_book(self):
        name=input('请输入您想借阅的书籍名称：')
        res=self.check_book(name)
        if res != None:
            print('经查询，流浪图书馆有该书籍')
            if res.state == 0:
                print('借阅成功')
                res.state == 1
            else:
                print('但十分抱歉，该图书已借出')
        else:
            print('十分抱歉，流浪图书馆暂未收录该图书')

    def return_book(self):
        name=input('请输入您想归还的书籍的名称（不要加书名号）：')
        res=self.check_book(name)
        if res != None:
            if res.state == 1:
                print('归还成功，希望您的这趟心灵之旅收获满满。')
            else:
                print('抱歉，经查询，本书非本馆借出。')
        else:
            print('抱歉，经查询，本书非本馆借出。')

    def show_author_book(self):
        author = input('你想找谁的书呢？')
        for i in self.authors:
            if i == author:
                print('%s的作品有：'%(author))
                for book in self.books:
                    if book.author==author:
                        print(book)
                    else:
                        continue
                break
            else:
                print('抱歉，我们还没有收录该作者的作品')

manager=BookManager()
manager.menu()
