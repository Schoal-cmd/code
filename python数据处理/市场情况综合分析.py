import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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
