import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义低饱和度的颜色方案
colors = ['#6BAED6', '#74C476', '#FFD699']  # 低饱和度的蓝色、浅绿色、浅黄色

# 创建一个大的图形窗口
plt.figure(figsize=(20, 30))

# 问题1：年龄分布（竖向条形图）
plt.subplot(7, 2, 1)
ages = ['18-25岁', '26-35岁', '36-45岁', '46-55岁', '56岁以上']
counts = [168, 65, 109, 111, 60]
bars = plt.bar(ages, counts, color=colors)
plt.title('您的年龄', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题2：家庭结构（竖向条形图）
plt.subplot(7, 2, 2)
family = ['是', '否']
counts = [470, 49]
bars = plt.bar(family, counts, color=colors)
plt.title('您家庭中是否有12岁以下儿童或65岁以上老人', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题3：蔬菜消费方式（横向条形图）
plt.subplot(7, 2, 3)
places = ['菜市场的商贩', '小型生鲜超市', '大型连锁超市', '街道旁小商贩', '专门的生鲜蔬菜网购平台', '较少直接购买蔬菜']
scores = [3.67, 3.38, 3.32, 3.13, 3.06, 2.9]
bars = plt.barh(places, scores, color=colors)
plt.title('您主要的蔬菜消费方式或场所是什么 (按照频率排序)', fontsize=14, fontweight='bold')
plt.xlabel('综合得分', fontsize=12)
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width}', ha='left', va='center')

# 问题4：蔬菜支出比例（竖向条形图）
plt.subplot(7, 2, 4)
expense = ['10%以下', '10-20%', '20-30%', '30%以上']
counts = [128, 172, 104, 115]
bars = plt.bar(expense, counts, color=colors)
plt.title('您家庭每月在蔬菜上的支出约占食品总支出的', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题5：购买关注点（横向条形图）
plt.subplot(7, 2, 5)
concerns = ['价格', '新鲜度', '是否有农药残留检测', '是否为有机/绿色认证', '品种新颖性', '其他']
counts = [388, 406, 289, 229, 194, 5]
bars = plt.barh(concerns, counts, color=colors)
plt.title('您购买蔬菜时最关注哪些方面?', fontsize=14, fontweight='bold')
plt.xlabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width}', ha='left', va='center')

# 问题6：健康影响（竖向条形图）
plt.subplot(7, 2, 6)
impact = ['非常重要', '比较重要', '一般', '不太重要']
counts = [219, 150, 90, 60]
bars = plt.bar(impact, counts, color=colors)
plt.title('您认为优质蔬菜对健康的影响程度是', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题7：品牌关注（竖向条形图）
plt.subplot(7, 2, 7)
brand_attention = ['会明确关注', '会大概关注', '不太关注']
counts = [240, 138, 141]
bars = plt.bar(brand_attention, counts, color=colors)
plt.title('您在购买蔬菜时是否会关注其品牌品类', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题8：固定购买习惯（竖向条形图）
plt.subplot(7, 2, 8)
habit = ['会，而且还会确认其品类是否属实', '会，但是只是大概确认', '不会刻意购买某一类']
counts = [245, 123, 151]
bars = plt.bar(habit, counts, color=colors)
plt.title('在您的购买习惯当中，是否会固定购买某一品牌品类的蔬菜', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
plt.xticks(rotation=15)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题9：认证蔬菜优势（横向条形图）
plt.subplot(7, 2, 9)
advantages = ['味道更好', '营养价值更高', '更为健康放心', '不如自种菜']
counts = [123, 121, 170, 105]
bars = plt.barh(advantages, counts, color=colors)
plt.title('您认为经过认证的优质蔬菜或知识产权保护的特定蔬菜品类对比一般蔬菜是否具有优势', fontsize=14, fontweight='bold')
plt.xlabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width}', ha='left', va='center')

# 问题10：餐饮单位使用认证蔬菜（竖向条形图）
plt.subplot(7, 2, 10)
restaurant = ['是的', '不需要，但是要公示蔬菜的产业源头', '完全不需要公示']
counts = [233, 201, 85]
bars = plt.bar(restaurant, counts, color=colors)
plt.title('您是否认为餐厅、饭堂等提供餐饮服务的单位应该使用经过认证的优质蔬菜', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
plt.xticks(rotation=15)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题11：绿色认证不符情况（竖向条形图）
plt.subplot(7, 2, 11)
mismatch = ['经常', '偶尔', '从未', '不关注蔬菜品种']
counts = [144, 162, 88, 125]
bars = plt.bar(mismatch, counts, color=colors)
plt.title('您是否遇到过购买的"绿色认证蔬菜"实际品质与宣传不符的情况', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题12：购买知名品牌意愿（竖向条形图）
plt.subplot(7, 2, 12)
preference = ['为了吃得好，愿意', '视品质提升程度而定', '更倾向选择无保护品种', '不了解']
counts = [172, 167, 79, 101]
bars = plt.bar(preference, counts, color=colors)
plt.title('相对于普通蔬菜，您是否愿意更倾向于购买知名品牌蔬菜', fontsize=14, fontweight='bold')
plt.ylabel('人数', fontsize=12)
plt.xticks(rotation=15)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}', ha='center', va='bottom')

# 问题13：种子产权保护影响（横向条形图）
plt.subplot(7, 2, 13)
impact = ['只是种子企业和研发机构遭到损失', '生劣种驱逐良种，对种植业会产生不利影响', '会直接不利于消费者的健康权益和消费权益']
counts = [160, 198, 161]
bars = plt.barh(impact, counts, color=colors)
plt.title('如果缺乏种子产权的保护，导致种子品类在市场上混同，您认为会侵犯到消费者权益吗?', fontsize=14, fontweight='bold')
plt.xlabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width}', ha='left', va='center')

# 问题14：支持自主知识产权蔬菜（横向条形图）
plt.subplot(7, 2, 14)
support = ['愿意长期购买支持', '短期尝试性支持', '需要对比性价比后选择', '不关注此因素']
counts = [160, 198, 161, 76]
bars = plt.barh(support, counts, color=colors)
plt.title('您是否愿意通过购买行为支持有自主知识产权的蔬菜品种', fontsize=14, fontweight='bold')
plt.xlabel('人数', fontsize=12)
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width}', ha='left', va='center')

# 调整布局
plt.tight_layout()
plt.show()



# 创建综合雷达图，展示市场机会
categories = ['健康认知度', '品牌关注度', '品牌忠诚度', '支付意愿', '创新支持度', 'B端需求']
values = [71.1, 72.83, 70.91, 65.32, 73.77, 83.62]  # 百分比数据

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]  # 闭合图形
angles += angles[:1]  # 闭合图形

# 创建雷达图
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.plot(angles, values, 'o-', linewidth=2, color='#FF9999')
ax.fill(angles, values, alpha=0.25, color='#FF9999')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])
ax.set_title('中高端健康蔬菜品牌市场机会评估', size=16, color='#333333', y=1.1)

plt.tight_layout()
plt.show()
