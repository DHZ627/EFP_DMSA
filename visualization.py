import numpy as np
import matplotlib.pyplot as plt
from parameters import *


# 可视化落点分布
# Visualize Impact Points
def visualize_impact_points(x_c, y_c, hit_probability, radius):
    """
    可视化EFP落点分布及目标区域
    Visualize the EFP impact points distribution and target area

    参数:
    x_c: numpy数组，形状为(n_samples,)，x方向落点坐标
    y_c: numpy数组，形状为(n_samples,)，y方向落点坐标
    hit_probability: float，命中概率
    radius: float，95%概率圆半径
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_c, y_c, alpha=0.6, s=5, label='落点分布 Impact Points')
    plt.gca().add_patch(plt.Rectangle((-target_width / 2, -target_height / 2), target_width, target_height,
                                      fill=False, edgecolor='r', linewidth=2, label='目标区域 Target Area'))
    plt.gca().add_patch(plt.Circle((0, 0), radius, fill=False, edgecolor='b', linestyle='--',
                                   linewidth=2, label='95%概率圆 95% Probability Circle'))

    # 添加命中概率文本
    # Add hit probability text
    plt.text(0.05, 0.95, f'命中概率: {hit_probability:.2%}',
             transform=plt.gca().transAxes, va='top', bbox=dict(boxstyle='round', fc='white', alpha=0.8))

    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('EFP落点分布及目标区域 EFP Impact Points Distribution and Target Area')
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.savefig('impact_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()


# 可视化敏感性分析结果
# Visualize Sensitivity Analysis Results
def visualize_sensitivity_analysis(df_global):
    """
    可视化全局敏感性分析结果
    Visualize the results of global sensitivity analysis

    参数:
    df_global: pandas DataFrame，包含参数敏感度数据
    """
    plt.figure(figsize=(10, 6))
    plt.barh(df_global['Parameter'], df_global['ST'], color='dodgerblue', label='总阶敏感度 Total Sensitivity')
    plt.barh(df_global['Parameter'], df_global['S1'], color='orange', alpha=0.7,
             label='一阶敏感度 First-order Sensitivity')

    # 添加数值标签
    # Add value labels
    for i, v in enumerate(df_global['ST']):
        plt.text(v + 0.01, i, f'{v:.3f}', va='center')
    for i, v in enumerate(df_global['S1']):
        plt.text(v + 0.01, i - 0.25, f'{v:.3f}', va='center')

    plt.gca().invert_yaxis()
    plt.title('全局敏感性分析（距目标中心距离）Global Sensitivity Analysis (Distance to Target Center)')
    plt.xlabel('敏感度指数 Sensitivity Index')
    plt.legend()
    plt.tight_layout()
    plt.savefig('sensitivity_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()