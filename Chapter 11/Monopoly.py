'''
绘制垄断市场补贴政策对无谓损失的影响图形
(Source: ECON1210 Weekly Quiz 11 Q1 / 2022 Spring Final Q65-69)
'''
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
Q = np.linspace(0, 300, 500)

# 需求曲线
P_demand = 146 - 0.5 * Q

# 边际成本
MC = np.full_like(Q, 4)

# 补贴后生产者面对的需求曲线
subsidy = 29
P_demand_subsidized = 146 - 0.5 * Q + subsidy  # = 175 - 0.5*Q

# 边际收益曲线
MR = 146 - Q
MR_subsidized = 175 - Q

# 关键点计算
# 1. 原垄断均衡
Q_monopoly = 142
P_monopoly = 146 - 0.5 * Q_monopoly

# 2. 社会最优（竞争均衡）
Q_competitive = 284
P_competitive = 4

# 3. 补贴后垄断均衡
Q_subsidy = 171
P_s_producer = 175 - 0.5 * Q_subsidy  # 生产者收到的价格
P_s_consumer = P_s_producer - subsidy  # 消费者支付的价格

# 创建图形
fig, ax = plt.subplots(figsize=(12, 8))

# 绘制曲线
ax.plot(Q, P_demand, 'b-', linewidth=2.5, label='原需求曲线 (消费者) $P_c = 146 - 0.5Q$')
ax.plot(Q, P_demand_subsidized, 'r-', linewidth=2.5, label=f'补贴后生产者面对需求曲线 $P_s = 175 - 0.5Q$')
ax.plot(Q, MC, 'g-', linewidth=2.5, label='边际成本 MC = 4')
ax.plot(Q, MR, 'b--', linewidth=1.5, alpha=0.7, label='原边际收益 MR = 146 - Q')
ax.plot(Q, MR_subsidized, 'r--', linewidth=1.5, alpha=0.7, label='补贴后边际收益 MR\' = 175 - Q')

# 标注关键点
# 原垄断点
ax.plot(Q_monopoly, P_monopoly, 'bo', markersize=10)
ax.annotate(f'A: 原垄断均衡\nQ={Q_monopoly}, P={P_monopoly}',
            xy=(Q_monopoly, P_monopoly),
            xytext=(Q_monopoly-50, P_monopoly+20),
            arrowprops=dict(arrowstyle='->', color='blue'),
            fontsize=10, color='blue')

# 补贴后均衡
ax.plot(Q_subsidy, P_s_consumer, 'ro', markersize=10)  # 消费者支付
ax.plot(Q_subsidy, P_s_producer, 'ro', markersize=10, fillstyle='none')  # 生产者收到
ax.annotate(f'Bc: 消费者支付\nQ={Q_subsidy}, P={P_s_consumer:.1f}',
            xy=(Q_subsidy, P_s_consumer),
            xytext=(Q_subsidy-40, P_s_consumer-15),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10, color='red')
ax.annotate(f'Bs: 生产者收到\nQ={Q_subsidy}, P={P_s_producer:.1f}',
            xy=(Q_subsidy, P_s_producer),
            xytext=(Q_subsidy+20, P_s_producer+10),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10, color='red')

# 社会最优点
ax.plot(Q_competitive, P_competitive, 'go', markersize=10)
ax.annotate(f'C: 社会最优\nQ={Q_competitive}, P={P_competitive}',
            xy=(Q_competitive, P_competitive),
            xytext=(Q_competitive-50, P_competitive+15),
            arrowprops=dict(arrowstyle='->', color='green'),
            fontsize=10, color='green')

# 补贴箭头
ax.annotate('', xy=(Q_subsidy, P_s_producer), 
            xytext=(Q_subsidy, P_s_consumer),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
ax.text(Q_subsidy+5, (P_s_producer + P_s_consumer)/2, 
        f'补贴\n{subsidy}美元', fontsize=10, color='purple', va='center')

# 填充无谓损失区域
# 补贴前的DWL（浅蓝色）
Q_dwl1 = np.linspace(Q_monopoly, Q_competitive, 100)
ax.fill_between(Q_dwl1, 4, 146-0.5*Q_dwl1, 
                alpha=0.2, color='blue', label=f'原无谓损失 = 5041')

# 补贴后的DWL（浅红色）
Q_dwl2 = np.linspace(Q_subsidy, Q_competitive, 100)
ax.fill_between(Q_dwl2, 4, 146-0.5*Q_dwl2, 
                alpha=0.3, color='red', label=f'补贴后无谓损失 = {0.5*(P_s_consumer-4)*(Q_competitive-Q_subsidy):.1f}')

# 添加垂直线
ax.vlines(x=Q_monopoly, ymin=0, ymax=P_monopoly, color='blue', linestyle=':', alpha=0.5)
ax.vlines(x=Q_subsidy, ymin=0, ymax=P_s_producer, color='red', linestyle=':', alpha=0.5)
ax.vlines(x=Q_competitive, ymin=0, ymax=146-0.5*Q_competitive, color='green', linestyle=':', alpha=0.5)

# 设置图形属性
ax.set_xlim(0, 300)
ax.set_ylim(0, 180)
ax.set_xlabel('数量 Q (百万单位/年)', fontsize=12)
ax.set_ylabel('价格 P (美元/单位)', fontsize=12)
ax.set_title('垄断市场补贴政策对无谓损失的影响', fontsize=14, fontweight='bold')

# 添加网格和图例
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

# 添加说明文本框
textstr = '\n'.join([
    '关键参数:',
    f'• 需求: P = 146 - 0.5Q',
    f'• 边际成本: MC = 4',
    f'• 补贴: {subsidy}美元/单位',
    '',
    '关键结果:',
    f'• 原垄断: Q={Q_monopoly}, P={P_monopoly}',
    f'• 补贴后: Q={Q_subsidy}, Pc={P_s_consumer:.1f}, Ps={P_s_producer:.1f}',
    f'• 社会最优: Q={Q_competitive}, P=4',
    f'• 补贴后DWL: {0.5*(P_s_consumer-4)*(Q_competitive-Q_subsidy):.1f}'
])

props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()