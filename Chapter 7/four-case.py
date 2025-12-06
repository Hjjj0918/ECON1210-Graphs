# Source: ECON1210 Question Bank 7 Q18
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义需求曲线和供给曲线
def demand_curve(q):
    return 100 - 2*q

def supply_curve(q):
    return 10 + q

# 计算均衡点
q_vals = np.linspace(0, 50, 500)
p_demand = demand_curve(q_vals)
p_supply = supply_curve(q_vals)

# 均衡数量和价格
q_eq = 30  # (100-2q = 10+q) => 90=3q => q=30
p_eq = 40  # 100-2*30=40

# 价格上限设置
p_ceiling = 25  # 低于均衡价格

# 价格上限下的成交量（由供给曲线决定）
q_ceiling = p_ceiling - 10  # 从供给曲线: 25 = 10 + q => q=15

# 价格上限下的最高支付意愿
p_max_willing = demand_curve(q_ceiling)  # 100-2*15=70

# 创建图形
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('价格上限下的四种分配机制', fontsize=16)

# 颜色定义
colors = {
    'demand': '#1f77b4',
    'supply': '#ff7f0e',
    'ceiling': '#d62728',
    'consumer_surplus': 'lightblue',
    'producer_surplus': 'lightcoral',
    'deadweight_loss': 'lightgray',
    'bribery': 'purple',
    'waste': 'brown'
}

# 情况1：理想分配（按支付意愿分配）
ax = axes[0, 0]
ax.plot(q_vals, p_demand, color=colors['demand'], label='需求曲线', lw=2)
ax.plot(q_vals, p_supply, color=colors['supply'], label='供给曲线', lw=2)
ax.axhline(p_ceiling, color=colors['ceiling'], linestyle='--', label=f'价格上限 (P={p_ceiling})')

# 标记均衡点
ax.plot(q_eq, p_eq, 'ko', markersize=8, label=f'均衡点 (Q={q_eq}, P={p_eq})')

# 价格上限下的成交量
ax.axvline(q_ceiling, color='gray', linestyle=':', alpha=0.5)

# 填充消费者剩余和生产者剩余
# 消费者剩余：需求曲线与价格上限之间的三角形
cs_q = np.array([0, q_ceiling, q_ceiling])
cs_p = np.array([p_max_willing, p_ceiling, p_ceiling])
cs_points = np.column_stack([cs_q, cs_p])
cs_poly = Polygon(cs_points, closed=True, color=colors['consumer_surplus'], alpha=0.5)
ax.add_patch(cs_poly)

# 生产者剩余：价格上限与供给曲线之间的三角形
ps_q = np.array([0, 0, q_ceiling])
ps_p = np.array([10, p_ceiling, p_ceiling])
ps_points = np.column_stack([ps_q, ps_p])
ps_poly = Polygon(ps_points, closed=True, color=colors['producer_surplus'], alpha=0.5)
ax.add_patch(ps_poly)

# 无谓损失
dwl_q = np.array([q_ceiling, q_ceiling, q_eq])
dwl_p = np.array([p_ceiling, demand_curve(q_ceiling), p_eq])
dwl_points = np.column_stack([dwl_q, dwl_p])
dwl_poly = Polygon(dwl_points, closed=True, color=colors['deadweight_loss'], alpha=0.5)
ax.add_patch(dwl_poly)

ax.set_xlim(0, 50)
ax.set_ylim(0, 110)
ax.set_xlabel('数量 (Q)')
ax.set_ylabel('价格 (P)')
ax.set_title('1. 理想分配（按支付意愿分配）')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# 添加文字说明
ax.text(5, 95, f'消费者剩余: {0.5*(p_max_willing-p_ceiling)*q_ceiling:.1f}', fontsize=9)
ax.text(5, 20, f'生产者剩余: {0.5*(p_ceiling-10)*q_ceiling:.1f}', fontsize=9)
ax.text(25, 45, f'无谓损失: {0.5*(p_eq-p_ceiling)*(q_eq-q_ceiling):.1f}', fontsize=9)

# 情况2：行贿分配
ax = axes[0, 1]
ax.plot(q_vals, p_demand, color=colors['demand'], label='需求曲线', lw=2)
ax.plot(q_vals, p_supply, color=colors['supply'], label='供给曲线', lw=2)
ax.axhline(p_ceiling, color=colors['ceiling'], linestyle='--', label=f'价格上限 (P={p_ceiling})')
ax.plot(q_eq, p_eq, 'ko', markersize=8, label=f'均衡点')
ax.axvline(q_ceiling, color='gray', linestyle=':', alpha=0.5)

# 行贿示意：实际支付价格 = 价格上限 + 贿赂
bribe_amount = 20  # 贿赂金额
effective_price = p_ceiling + bribe_amount

# 填充区域
# 生产者剩余（不变）
ps_poly2 = Polygon(ps_points, closed=True, color=colors['producer_surplus'], alpha=0.5)
ax.add_patch(ps_poly2)

# 消费者剩余减少（因为支付了贿赂）
# 剩余变为需求曲线与实际支付价格之间的区域
cs_bribe_q = np.array([0, q_ceiling, q_ceiling])
cs_bribe_p = np.array([p_max_willing, effective_price, effective_price])
cs_bribe_points = np.column_stack([cs_bribe_q, cs_bribe_p])
cs_bribe_poly = Polygon(cs_bribe_points, closed=True, color=colors['consumer_surplus'], alpha=0.5)
ax.add_patch(cs_bribe_poly)

# 贿赂转移（从消费者到官员）
bribe_rect = plt.Rectangle((0, p_ceiling), q_ceiling, bribe_amount, 
                          color=colors['bribery'], alpha=0.5, label='贿赂转移')
ax.add_patch(bribe_rect)

ax.set_xlim(0, 50)
ax.set_ylim(0, 110)
ax.set_xlabel('数量 (Q)')
ax.set_ylabel('价格 (P)')
ax.set_title('2. 行贿分配')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

ax.text(5, 95, f'消费者净剩余: {0.5*(p_max_willing-effective_price)*q_ceiling:.1f}', fontsize=9)
ax.text(5, 30, f'贿赂转移: {bribe_amount*q_ceiling:.1f}', fontsize=9)
ax.text(25, 45, f'生产者剩余不变', fontsize=9)

# 情况3：浪费性竞争
ax = axes[1, 0]
ax.plot(q_vals, p_demand, color=colors['demand'], label='需求曲线', lw=2)
ax.plot(q_vals, p_supply, color=colors['supply'], label='供给曲线', lw=2)
ax.axhline(p_ceiling, color=colors['ceiling'], linestyle='--', label=f'价格上限 (P={p_ceiling})')
ax.plot(q_eq, p_eq, 'ko', markersize=8, label=f'均衡点')
ax.axvline(q_ceiling, color='gray', linestyle=':', alpha=0.5)

# 浪费性竞争示意：资源浪费
waste_per_unit = 15  # 每单位的竞争成本

# 生产者剩余（不变）
ps_poly3 = Polygon(ps_points, closed=True, color=colors['producer_surplus'], alpha=0.5)
ax.add_patch(ps_poly3)

# 消费者剩余（考虑浪费成本后的净剩余）
cs_waste_q = np.array([0, q_ceiling, q_ceiling])
cs_waste_p = np.array([p_max_willing, p_ceiling+waste_per_unit, p_ceiling+waste_per_unit])
cs_waste_points = np.column_stack([cs_waste_q, cs_waste_p])
cs_waste_poly = Polygon(cs_waste_points, closed=True, color=colors['consumer_surplus'], alpha=0.5)
ax.add_patch(cs_waste_poly)

# 浪费的区域（无谓损失增加）
waste_rect = plt.Rectangle((0, p_ceiling), q_ceiling, waste_per_unit, 
                          color=colors['waste'], alpha=0.5, label='竞争浪费')
ax.add_patch(waste_rect)

ax.set_xlim(0, 50)
ax.set_ylim(0, 110)
ax.set_xlabel('数量 (Q)')
ax.set_ylabel('价格 (P)')
ax.set_title('3. 浪费性竞争（如排队）')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

ax.text(5, 95, f'消费者净剩余: {0.5*(p_max_willing-(p_ceiling+waste_per_unit))*q_ceiling:.1f}', fontsize=9)
ax.text(5, 30, f'浪费成本: {waste_per_unit*q_ceiling:.1f}', fontsize=9)
ax.text(25, 45, f'社会总剩余减少', fontsize=9)

# 情况4：随机分配（未分配给评价最高者）
ax = axes[1, 1]
ax.plot(q_vals, p_demand, color=colors['demand'], label='需求曲线', lw=2)
ax.plot(q_vals, p_supply, color=colors['supply'], label='供给曲线', lw=2)
ax.axhline(p_ceiling, color=colors['ceiling'], linestyle='--', label=f'价格上限 (P={p_ceiling})')
ax.plot(q_eq, p_eq, 'ko', markersize=8, label=f'均衡点')
ax.axvline(q_ceiling, color='gray', linestyle=':', alpha=0.5)

# 生产者剩余（不变）
ps_poly4 = Polygon(ps_points, closed=True, color=colors['producer_surplus'], alpha=0.5)
ax.add_patch(ps_poly4)

# 随机分配下的消费者剩余（低于理想分配）
# 假设平均支付意愿降低
avg_willingness = (p_max_willing + p_ceiling) / 2  # 随机分配下的平均支付意愿

cs_random_q = np.array([0, q_ceiling, q_ceiling])
cs_random_p = np.array([avg_willingness, p_ceiling, p_ceiling])
cs_random_points = np.column_stack([cs_random_q, cs_random_p])
cs_random_poly = Polygon(cs_random_points, closed=True, color=colors['consumer_surplus'], alpha=0.5)
ax.add_patch(cs_random_poly)

# 效率损失区域
efficiency_loss_q = np.array([0, 0, q_ceiling, q_ceiling])
efficiency_loss_p = np.array([p_max_willing, avg_willingness, p_ceiling, p_ceiling])
efficiency_loss_points = np.column_stack([efficiency_loss_q, efficiency_loss_p])
efficiency_loss_poly = Polygon(efficiency_loss_points, closed=True, color='yellow', alpha=0.3, label='分配效率损失')
ax.add_patch(efficiency_loss_poly)

ax.set_xlim(0, 50)
ax.set_ylim(0, 110)
ax.set_xlabel('数量 (Q)')
ax.set_ylabel('价格 (P)')
ax.set_title('4. 随机分配（未给评价最高者）')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

ax.text(5, 95, f'消费者剩余: {0.5*(avg_willingness-p_ceiling)*q_ceiling:.1f}', fontsize=9)
ax.text(5, 30, f'分配效率损失', fontsize=9)
ax.text(25, 45, f'生产者剩余不变', fontsize=9)

plt.tight_layout()
plt.show()

# 打印关键数据对比
print("=== 价格上限下四种情况的对比 ===")
print(f"价格上限: P={p_ceiling}")
print(f"成交量: Q={q_ceiling}")
print(f"均衡: Q={q_eq}, P={p_eq}")
print()
print("生产者剩余在不同情况下的值:")
ps_ideal = 0.5*(p_ceiling-10)*q_ceiling
print(f"情况1(理想): {ps_ideal:.1f}")
print(f"情况2(行贿): {ps_ideal:.1f}")
print(f"情况3(浪费): {ps_ideal:.1f}")
print(f"情况4(随机): {ps_ideal:.1f}")
print()
print("结论: 生产者剩余在所有情况下都相同")