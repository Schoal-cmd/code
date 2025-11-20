from collections import defaultdict

# 创建一个defaultdict，其默认值为0
right = defaultdict(int)

# 尝试访问一个不存在的键，它会自动被初始化为默认值0
print(right['a'])  # 输出: 0

# 现在，我们可以给这个键赋值，并增加它的值
right['a'] += 1
print(right['a'])  # 输出: 1

# 访问另一个不存在的键，它同样会被初始化为默认值0
right['b'] += 1
print(right['b'])  # 输出: 1

# 打印整个字典
print(right)  # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 1})






from collections import Counter

# 创建一个包含水果名称的列表
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 创建一个Counter对象，并传入列表进行计数
fruit_count = Counter(fruits)

# 打印结果
print(fruit_count)


##更新数据
# 新的水果数据
new_fruits = ['banana', 'kiwi', 'apple', 'orange', 'kiwi']

# 更新之前的Counter对象
fruit_count.update(new_fruits)

# 打印更新后的结果
print(fruit_count)






##复合使用，优化嵌套计数
from collections import defaultdict, Counter
print('///')
# 假设我们有三个篮子，每个篮子包含一些水果
baskets = [
    ['apple', 'banana', 'apple'],
    ['orange', 'banana', 'banana'],
    ['apple', 'apple']
]

# 创建一个 defaultdict，其默认值是 Counter
fruit_count = defaultdict(Counter)
print(fruit_count)
# 遍历每个篮子
for basket_id, fruits in enumerate(baskets):
    # 遍历篮子里的每种水果
    for fruit in fruits:
        # 使用 defaultdict(Counter) 的特性：如果键不存在，则自动创建一个 Counter 对象
        # 然后，增加对应水果的计数
        fruit_count[basket_id][fruit] += 1
print(fruit_count)
# 输出结果
for basket_id, counter in fruit_count.items():
    print(f"Basket {basket_id}: {dict(counter)}")
