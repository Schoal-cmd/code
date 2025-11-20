import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体和颜色方案
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#6A0572', '#1A535C', '#FF9F1C', '#2EC4B6', '#E71D36', '#FF9F1C', '#2EC4B6']

# 创建图表布局
fig = plt.figure(figsize=(20, 30))
fig.suptitle('健康蔬菜品牌市场调研数据分析', fontsize=20, y=1.02)

# 1. 年龄分布
ax1 = plt.subplot(5, 3, 1)
age_groups = ['18-25岁', '26-35岁', '36-45岁', '46-55岁', '56岁以上']
age_counts = [168, 65, 109, 111, 60]
ax1.pie(age_counts, labels=age_groups, autopct='%1.1f%%', colors=colors[:5])
ax1.set_title('年龄分布')

# 2. 家庭结构
ax2 = plt.subplot(5, 3, 2)
family_structure = ['有12岁以下儿童或65岁以上老人', '没有']
family_counts = [470, 49]
ax2.pie(family_counts, labels=family_structure, autopct='%1.1f%%', colors=colors[:2])
ax2.set_title('家庭结构')

# 3. 蔬菜消费方式或场所
ax3 = plt.subplot(5, 3, 3)
consumption_places = ['菜市场的商贩', '小型生鲜超市', '大型连锁超市', '街道旁小商贩', '专门的生鲜蔬菜网购平台', '较少直接购买蔬菜']
consumption_scores = [3.67, 3.38, 3.32, 3.13, 3.06, 2.9]
ax3.barh(consumption_places, consumption_scores, color=colors[:6])
ax3.set_title('蔬菜消费方式或场所（综合得分）')
ax3.set_xlabel('综合得分')

# 4. 蔬菜支出占比
ax4 = plt.subplot(5, 3, 4)
expense_ratio = ['10%以下', '10-20%', '20-30%', '30%以上']
expense_counts = [128, 172, 104, 115]
ax4.pie(expense_counts, labels=expense_ratio, autopct='%1.1f%%', colors=colors[:4])
ax4.set_title('蔬菜支出占食品总支出比例')

# 5. 购买蔬菜关注点
ax5 = plt.subplot(5, 3, 5)
concerns = ['价格', '新鲜度', '农药残留检测', '有机/绿色认证', '品种新颖性']
concern_counts = [388, 406, 289, 229, 194]
ax5.barh(concerns, concern_counts, color=colors[:5])
ax5.set_title('购买蔬菜关注点')
ax5.set_xlabel('人数')

# 6. 优质蔬菜对健康的影响
ax6 = plt.subplot(5, 3, 6)
health_impact = ['非常重要', '比较重要', '一般', '不太重要']
impact_counts = [219, 150, 90, 60]
ax6.pie(impact_counts, labels=health_impact, autopct='%1.1f%%', colors=colors[:4])
ax6.set_title('优质蔬菜对健康的影响程度')

# 7. 购买蔬菜时关注品牌
ax7 = plt.subplot(5, 3, 7)
brand_attention = ['明确关注品牌和生产地', '大概关注品牌', '不太关注']
attention_counts = [240, 138, 141]
ax7.pie(attention_counts, labels=brand_attention, autopct='%1.1f%%', colors=colors[:3])
ax7.set_title('购买蔬菜时关注品牌情况')

# 8. 固定购买品牌品类
ax8 = plt.subplot(5, 3, 8)
fixed_purchase = ['会确认品类属实', '会大概确认', '不会刻意购买']
purchase_counts = [245, 123, 151]
ax8.pie(purchase_counts, labels=fixed_purchase, autopct='%1.1f%%', colors=colors[:3])
ax8.set_title('固定购买品牌品类情况')

# 9. 认证优质蔬菜的优势
ax9 = plt.subplot(5, 3, 9)
advantages = ['更为健康放心', '味道更好', '营养价值更高', '不如自种菜']
advantage_counts = [170, 123, 121, 105]
ax9.pie(advantage_counts, labels=advantages, autopct='%1.1f%%', colors=colors[:4])
ax9.set_title('认证优质蔬菜的优势认知')

# 10. 餐饮服务单位使用认证蔬菜
ax10 = plt.subplot(5, 3, 10)
restaurant_opinion = ['应该使用认证蔬菜', '不需要但要公示源头', '完全不需要公示']
opinion_counts = [233, 201, 85]
ax10.pie(opinion_counts, labels=restaurant_opinion, autopct='%1.1f%%', colors=colors[:3])
ax10.set_title('餐饮服务单位使用认证蔬菜态度')

# 11. 遇到认证蔬菜与宣传不符
ax11 = plt.subplot(5, 3, 11)
misleading = ['经常', '偶尔', '从未', '不关注品种']
misleading_counts = [144, 162, 88, 125]
ax11.pie(misleading_counts, labels=misleading, autopct='%1.1f%%', colors=colors[:4])
ax11.set_title('遇到认证蔬菜与宣传不符情况')

# 12. 购买知名品牌蔬菜意愿
ax12 = plt.subplot(5, 3, 12)
brand_willingness = ['愿意', '视品质而定', '倾向无保护品种', '不了解']
willingness_counts = [172, 167, 79, 101]
ax12.pie(willingness_counts, labels=brand_willingness, autopct='%1.1f%%', colors=colors[:4])
ax12.set_title('购买知名品牌蔬菜意愿')

# 13. 种子产权保护对消费者权益影响
ax13 = plt.subplot(5, 3, 13)
seed_protection = ['影响消费者权益', '生劣种驱逐良种', '只影响种子企业']
protection_counts = [183, 138, 122]
ax13.pie(protection_counts, labels=seed_protection, autopct='%1.1f%%', colors=colors[:3])
ax13.set_title('种子产权保护对消费者权益影响认知')

# 14. 支持有自主知识产权蔬菜品种
ax14 = plt.subplot(5, 3, 14)
support_ip = ['愿意长期购买支持', '短期尝试性支持', '需要对比性价比', '不关注此因素']
support_counts = [160, 198, 161, 76]
ax14.pie(support_counts, labels=support_ip, autopct='%1.1f%%', colors=colors[:4])
ax14.set_title('支持有自主知识产权蔬菜品种意愿')

plt.tight_layout()
plt.show()
