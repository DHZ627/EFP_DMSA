import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from SALib.sample import saltelli
from SALib.analyze import sobol
import pandas as pd
from parameters import *
from model import *
from visualization import *


def main():
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Set Chinese font
    plt.rcParams['axes.unicode_minus'] = False  # Solve the problem of negative sign display

    # 蒙特卡洛仿真
    print("开始蒙特卡洛仿真...")
    x_c, y_c = monte_carlo_simulation()

    # 计算命中概率和95%概率圆半径
    hit_probability = calculate_hit_probability(x_c, y_c)
    radius = calculate_95_percent_circle_radius(x_c, y_c)

    # 可视化落点分布
    visualize_impact_points(x_c, y_c, hit_probability, radius)

    print(f"命中概率: {hit_probability:.2%}")
    print(f"95%概率圆半径: {radius:.2f} m\n")

    # Sobol全局敏感性分析
    print("开始Sobol全局敏感性分析...")
    problem = {
        'num_vars': 9,
        'names': ['vx', 'vy', 'T1_sim', 'theta0', 'phi0',
                  'dtheta_dt', 'dphi_dt', 'EFP_error_x', 'EFP_error_y'],
        'bounds': [[0, 1]] * 9
    }

    N = 1024  # 增加样本量提高精度
    param_values = saltelli.sample(problem, N)
    param_values = np.clip(param_values, 1e-9, 1 - 1e-9)
    param_values_conv = convert_samples(param_values)

    # 计算输出
    output = model(param_values_conv)

    # 敏感性分析
    Si = sobol.analyze(problem, output, print_to_console=False)

    # 结果处理
    df_global = pd.DataFrame({
        'Parameter': problem['names'],
        'S1': Si['S1'],
        'ST': Si['ST']
    }).sort_values('ST', ascending=False)

    # 保存结果
    df_global.to_csv('global_sobol.csv', index=False)

    # 打印结果
    print("全局敏感度排序（距目标中心距离）：")
    print(df_global[['Parameter', 'S1', 'ST']].to_string(index=False))

    # 可视化
    visualize_sensitivity_analysis(df_global)


if __name__ == "__main__":
    main()    