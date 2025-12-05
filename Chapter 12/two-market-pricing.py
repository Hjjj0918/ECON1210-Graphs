import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 设置中文和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 定义参数
MC = 9
# 亚洲需求: Q = 46 - 0.5P -> P = 92 - 2Q
# 欧洲需求: Q = 32 - 0.5P -> P = 64 - 2Q

# 计算统一定价
def single_price():
    # 总需求: Q_total = 78 - P
    P_single = 43.5
    Q_total = 78 - P_single
    Q_asia_single = 46 - 0.5*P_single
    Q_europe_single = 32 - 0.5*P_single
    return P_single, Q_asia_single, Q_europe_single

# 计算双定价
def dual_price():
    # 亚洲: MR = 92 - 4Q = 9 -> Q = 20.75, P = 50.5
    # 欧洲: MR = 64 - 4Q = 9 -> Q = 13.75, P = 36.5
    P_asia_dual = 50.5
    P_europe_dual = 36.5
    Q_asia_dual = 20.75
    Q_europe_dual = 13.75
    return P_asia_dual, P_europe_dual, Q_asia_dual, Q_europe_dual

# 获取价格和数量
P_single, Q_asia_single, Q_europe_single = single_price()
P_asia_dual, P_europe_dual, Q_asia_dual, Q_europe_dual = dual_price()

# 计算消费者剩余
def calculate_cs(P, Q_max, Q_actual, slope):
    """计算消费者剩余"""
    P_max = P + (Q_max - Q_actual) * abs(1/slope)  # 反需求函数的截距
    cs = 0.5 * (P_max - P) * Q_actual
    return cs

# 计算亚洲市场消费者剩余变化
# 亚洲反需求斜率: dP/dQ = -2, 所以斜率绝对值为2
# 单一定价下CS
P_max_asia = 92  # 当Q=0时
cs_asia_single = 0.5 * (P_max_asia - P_single) * Q_asia_single
cs_asia_dual = 0.5 * (P_max_asia - P_asia_dual) * Q_asia_dual

# 欧洲市场消费者剩余变化
P_max_europe = 64  # 当Q=0时
cs_europe_single = 0.5 * (P_max_europe - P_single) * Q_europe_single
cs_europe_dual = 0.5 * (P_max_europe - P_europe_dual) * Q_europe_dual

print(f"统一定价: P=${P_single}")
print(f"亚洲: Q={Q_asia_single:.2f}, CS=${cs_asia_single:.2f}百万")
print(f"欧洲: Q={Q_europe_single:.2f}, CS=${cs_europe_single:.2f}百万")
print()
print(f"双定价:")
print(f"亚洲: P=${P_asia_dual}, Q={Q_asia_dual:.2f}, CS=${cs_asia_dual:.2f}百万")
print(f"欧洲: P=${P_europe_dual}, Q={Q_europe_dual:.2f}, CS=${cs_europe_dual:.2f}百万")
print()
print(f"亚洲消费者剩余变化: ${cs_asia_single - cs_asia_dual:.2f}百万")
print(f"欧洲消费者剩余变化: ${cs_europe_dual - cs_europe_single:.2f}百万")

# 创建图形
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 设置颜色
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
cs_color = '#ffcccc'
highlight_color = '#ff6b6b'

# 1. 统一定价 - 亚洲市场
ax1 = axes[0, 0]
Q_asia = np.linspace(0, 46, 200)
P_asia = 92 - 2*Q_asia
ax1.plot(Q_asia, P_asia, 'b-', linewidth=2, label='需求曲线')
ax1.axhline(y=P_single, color='r', linestyle='--', linewidth=1.5, label=f'价格=${P_single}')
ax1.axvline(x=Q_asia_single, color='g', linestyle='--', linewidth=1, label=f'数量={Q_asia_single:.2f}')
ax1.fill_between(Q_asia[Q_asia <= Q_asia_single], P_single, P_asia[Q_asia <= Q_asia_single], 
                 color=cs_color, alpha=0.5, label='消费者剩余')
ax1.set_xlabel('数量 (百万单位)')
ax1.set_ylabel('价格 ($)')
ax1.set_title('统一定价 - 亚洲市场')
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 100)
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. 统一定价 - 欧洲市场
ax2 = axes[0, 1]
Q_europe = np.linspace(0, 32, 200)
P_europe = 64 - 2*Q_europe
ax2.plot(Q_europe, P_europe, 'b-', linewidth=2, label='需求曲线')
ax2.axhline(y=P_single, color='r', linestyle='--', linewidth=1.5, label=f'价格=${P_single}')
ax2.axvline(x=Q_europe_single, color='g', linestyle='--', linewidth=1, label=f'数量={Q_europe_single:.2f}')
ax2.fill_between(Q_europe[Q_europe <= Q_europe_single], P_single, P_europe[Q_europe <= Q_europe_single], 
                 color=cs_color, alpha=0.5, label='消费者剩余')
ax2.set_xlabel('数量 (百万单位)')
ax2.set_ylabel('价格 ($)')
ax2.set_title('统一定价 - 欧洲市场')
ax2.set_xlim(0, 35)
ax2.set_ylim(0, 70)
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. 总市场统一定价
ax3 = axes[0, 2]
Q_total = np.linspace(0, 78, 200)
P_total = 78 - Q_total
ax3.plot(Q_total, P_total, 'purple', linewidth=2, label='总需求曲线')
ax3.axhline(y=P_single, color='r', linestyle='--', linewidth=1.5, label=f'统一定价=${P_single}')
ax3.axvline(x=Q_asia_single+Q_europe_single, color='g', linestyle='--', linewidth=1, 
           label=f'总数量={Q_asia_single+Q_europe_single:.2f}')
ax3.set_xlabel('总数量 (百万单位)')
ax3.set_ylabel('价格 ($)')
ax3.set_title('统一定价 - 总市场')
ax3.set_xlim(0, 80)
ax3.set_ylim(0, 80)
ax3.legend()
ax3.grid(True, alpha=0.3)

# 4. 双定价 - 亚洲市场
ax4 = axes[1, 0]
ax4.plot(Q_asia, P_asia, 'b-', linewidth=2, label='需求曲线')
ax4.axhline(y=P_asia_dual, color='r', linestyle='--', linewidth=1.5, label=f'价格=${P_asia_dual}')
ax4.axvline(x=Q_asia_dual, color='g', linestyle='--', linewidth=1, label=f'数量={Q_asia_dual:.2f}')
# 用不同颜色突出显示消费者剩余
vertices = [(0, P_max_asia), (0, P_asia_dual), (Q_asia_dual, P_asia_dual), (Q_asia_dual, 92-2*Q_asia_dual)]
poly = Polygon(vertices, facecolor=highlight_color, alpha=0.6, label='消费者剩余')
ax4.add_patch(poly)
ax4.set_xlabel('数量 (百万单位)')
ax4.set_ylabel('价格 ($)')
ax4.set_title('双定价 - 亚洲市场 (CS较小)')
ax4.set_xlim(0, 50)
ax4.set_ylim(0, 100)
ax4.legend()
ax4.grid(True, alpha=0.3)

# 5. 双定价 - 欧洲市场
ax5 = axes[1, 1]
ax5.plot(Q_europe, P_europe, 'b-', linewidth=2, label='需求曲线')
ax5.axhline(y=P_europe_dual, color='r', linestyle='--', linewidth=1.5, label=f'价格=${P_europe_dual}')
ax5.axvline(x=Q_europe_dual, color='g', linestyle='--', linewidth=1, label=f'数量={Q_europe_dual:.2f}')
# 用不同颜色突出显示消费者剩余
vertices_eu = [(0, P_max_europe), (0, P_europe_dual), (Q_europe_dual, P_europe_dual), (Q_europe_dual, 64-2*Q_europe_dual)]
poly_eu = Polygon(vertices_eu, facecolor=highlight_color, alpha=0.6, label='消费者剩余')
ax5.add_patch(poly_eu)
ax5.set_xlabel('数量 (百万单位)')
ax5.set_ylabel('价格 ($)')
ax5.set_title('双定价 - 欧洲市场 (CS较大)')
ax5.set_xlim(0, 35)
ax5.set_ylim(0, 70)
ax5.legend()
ax5.grid(True, alpha=0.3)

# 6. 消费者剩余对比 (亚洲和欧洲)
ax6 = axes[1, 2]
categories = ['亚洲-统一定价', '亚洲-双定价', '欧洲-统一定价', '欧洲-双定价']
cs_values = [cs_asia_single, cs_asia_dual, cs_europe_single, cs_europe_dual]
colors_bar = [colors[0], colors[1], colors[0], colors[1]]
bars = ax6.bar(categories, cs_values, color=colors_bar, alpha=0.7)

# 添加数值标签
for bar, value in zip(bars, cs_values):
    height = bar.get_height()
    ax6.text(bar.get_x() + bar.get_width()/2., height,
             f'{value:.1f}', ha='center', va='bottom')

# 突出显示最后一题讨论的消费者剩余变化区域
# 在亚洲部分添加箭头和说明
ax6.annotate('亚洲消费者:\n愿意花$157.5M\n游说统一定价', 
             xy=(0.5, (cs_asia_single + cs_asia_dual)/2),
             xytext=(0, 300),
             arrowprops=dict(arrowstyle='->', color='red'),
             ha='center')

# 在欧洲部分添加箭头和说明
ax6.annotate('欧洲消费者:\n愿意花$84M\n游说双定价', 
             xy=(2.5, (cs_europe_single + cs_europe_dual)/2),
             xytext=(3, 300),
             arrowprops=dict(arrowstyle='->', color='green'),
             ha='center')

ax6.set_xlabel('定价制度')
ax6.set_ylabel('消费者剩余 (百万$)')
ax6.set_title('消费者剩余对比 (d)(e)题重点分析)')
ax6.grid(True, alpha=0.3, axis='y')
ax6.set_ylim(0, max(cs_values)*1.2)

# 添加总标题
plt.suptitle('Microsoft Windows定价策略分析: 统一定价 vs 双定价', fontsize=16, fontweight='bold')
plt.tight_layout()

# 保存图像
plt.savefig('microsoft_pricing_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# 打印详细计算结果
print("\n" + "="*60)
print("消费者剩余详细计算:")
print("="*60)
print(f"亚洲市场:")
print(f"  统一定价: 价格=${P_single}, 数量={Q_asia_single:.2f}M")
print(f"    消费者剩余 = 0.5 × (92 - {P_single}) × {Q_asia_single:.2f}")
print(f"               = 0.5 × {92-P_single:.1f} × {Q_asia_single:.2f}")
print(f"               = ${cs_asia_single:.2f}百万")
print()
print(f"  双定价: 价格=${P_asia_dual}, 数量={Q_asia_dual:.2f}M")
print(f"    消费者剩余 = 0.5 × (92 - {P_asia_dual}) × {Q_asia_dual:.2f}")
print(f"               = 0.5 × {92-P_asia_dual:.1f} × {Q_asia_dual:.2f}")
print(f"               = ${cs_asia_dual:.2f}百万")
print()
print(f"  亚洲消费者剩余变化: ${cs_asia_single:.2f} - ${cs_asia_dual:.2f} = ${cs_asia_single-cs_asia_dual:.2f}百万")
print(f"  所以亚洲消费者愿意花${cs_asia_single-cs_asia_dual:.2f}百万游说统一定价")
print()
print(f"欧洲市场:")
print(f"  统一定价: 价格=${P_single}, 数量={Q_europe_single:.2f}M")
print(f"    消费者剩余 = 0.5 × (64 - {P_single}) × {Q_europe_single:.2f}")
print(f"               = 0.5 × {64-P_single:.1f} × {Q_europe_single:.2f}")
print(f"               = ${cs_europe_single:.2f}百万")
print()
print(f"  双定价: 价格=${P_europe_dual}, 数量={Q_europe_dual:.2f}M")
print(f"    消费者剩余 = 0.5 × (64 - {P_europe_dual}) × {Q_europe_dual:.2f}")
print(f"               = 0.5 × {64-P_europe_dual:.1f} × {Q_europe_dual:.2f}")
print(f"               = ${cs_europe_dual:.2f}百万")
print()
print(f"  欧洲消费者剩余变化: ${cs_europe_dual:.2f} - ${cs_europe_single:.2f} = ${cs_europe_dual-cs_europe_single:.2f}百万")
print(f"  所以欧洲消费者愿意花${cs_europe_dual-cs_europe_single:.2f}百万游说双定价")