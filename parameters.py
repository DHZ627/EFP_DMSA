# 参数配置模块
# Parameter Configuration Module
import numpy as np
# 仿真参数
# Simulation Parameters
num_simulations = 10000  # 仿真次数 Number of simulations

# 固定参数
# Fixed Parameters
y0 = 30  # 打击高度 (m) Strike height
Vp = 2000  # EFP平均飞行速度 (m/s) Average flight speed of EFP
C_l = 0.3  # 战斗部中心到弹体质心的距离 (m) Distance from warhead center to projectile centroid
T1 = 0.1  # 识别时延 (s) Recognition delay
T2 = 55e-6  # 起爆时延 (s) Initiation delay

# 初始参数
# Initial Parameters
vx_init = 0  # 初始x方向速度 Initial velocity in x direction
vy_init = 0  # 初始y方向速度 Initial velocity in y direction
theta_init = np.deg2rad(0)  # 初始俯仰角 Initial pitch angle
phi_init = np.deg2rad(0)  # 初始偏航角 Initial yaw angle
psi_init = np.deg2rad(0)  # 初始滚转角 Initial roll angle

# 误差参数
# Error Parameters
sigma_vx = 0.25  # x方向速度标准差 Standard deviation of velocity in x direction (m/s)
sigma_vy = 0.25  # y方向速度标准差 Standard deviation of velocity in y direction (m/s)
sigma_EFP = np.deg2rad(0.1)  # EFP误差标准差 EFP error standard deviation (rad)
sigma_T1 = 0.01  # 识别时延标准差 Recognition delay standard deviation (s)

# 扰动参数
# Disturbance Parameters
sigma_theta = np.deg2rad(1.5)  # 俯仰角标准差 Pitch angle standard deviation (rad)
sigma_phi = np.deg2rad(1.5)  # 偏航角标准差 Yaw angle standard deviation (rad)
sigma_psi = np.deg2rad(0)  # 滚转角标准差 Roll angle standard deviation (rad)
sigma_dtheta_dt = np.deg2rad(1.5)  # 俯仰角变化率标准差 Pitch rate standard deviation (rad/s)
sigma_dphi_dt = np.deg2rad(1.5)  # 偏航角变化率标准差 Yaw rate standard deviation (rad/s)
sigma_dpsi_dt = np.deg2rad(0)  # 滚转角变化率标准差 Roll rate standard deviation (rad/s)

# 目标参数
# Target Parameters
target_width = 7.9  # 目标宽度 Target width (m)
target_height = 3.6  # 目标高度 Target height (m)