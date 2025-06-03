import numpy as np
from scipy.stats import norm
from parameters import *


# 参数转换函数
# Parameter Conversion Function
def convert_samples(params):
    """
    将均匀分布的样本转换为正态分布的参数值
    Convert uniformly distributed samples to normally distributed parameter values

    参数:
    params: numpy数组，形状为(n_samples, n_params)，均匀分布的样本
    params: numpy array with shape (n_samples, n_params), uniformly distributed samples

    返回:
    converted: numpy数组，形状为(n_samples, n_params)，正态分布的参数值
    converted: numpy array with shape (n_samples, n_params), normally distributed parameter values
    """
    converted = np.zeros_like(params)
    # vx ~ N(0, 1)
    converted[:, 0] = norm.ppf(params[:, 0], 0, 1)
    # vy ~ N(0, 1)
    converted[:, 1] = norm.ppf(params[:, 1], 0, 1)
    # T1_sim ~ N(0.1, 0.01)
    converted[:, 2] = norm.ppf(params[:, 2], 0.1, 0.01)
    # theta0 ~ N(0, 1.5°)
    converted[:, 3] = norm.ppf(params[:, 3], 0, np.deg2rad(1.5))
    # phi0 ~ N(0, 1.5°)
    converted[:, 4] = norm.ppf(params[:, 4], 0, np.deg2rad(1.5))
    # dtheta_dt ~ N(0, 1.5°/s)
    converted[:, 5] = norm.ppf(params[:, 5], 0, np.deg2rad(1.5))
    # dphi_dt ~ N(0, 1.5°/s)
    converted[:, 6] = norm.ppf(params[:, 6], 0, np.deg2rad(1.5))
    # EFP_error_x ~ N(0, 0.5°)
    converted[:, 7] = norm.ppf(params[:, 7], 0, np.deg2rad(0.5))
    # EFP_error_y ~ N(0, 0.5°)
    converted[:, 8] = norm.ppf(params[:, 8], 0, np.deg2rad(0.5))
    return converted


# 模型函数
# Model Function
def model(params):
    """
    计算EFP的落点坐标和到目标中心的距离
    Calculate the impact coordinates of EFP and the distance to the target center

    参数:
    params: numpy数组，形状为(n_samples, n_params)，模型参数
    params: numpy array with shape (n_samples, n_params), model parameters

    返回:
    distance: numpy数组，形状为(n_samples,)，到目标中心的距离
    distance: numpy array with shape (n_samples,), distance to the target center
    """
    y0 = 30
    Vp = 2000
    C_l = 0.3
    T2 = 55e-6
    psi0 = 0

    vx, vy, T1_sim, theta0, phi0, dtheta_dt, dphi_dt, EFP_x, EFP_y = params.T

    cos_theta0 = np.cos(theta0)
    T3 = y0 / (cos_theta0 * Vp)
    Delta_t = T1_sim + T2

    # 计算牵连速度
    # Calculate the convective velocity
    cos_psi0 = np.cos(psi0)
    sin_psi0 = np.sin(psi0)
    sin_theta0 = np.sin(theta0)
    sin_phi0 = np.sin(phi0)
    cos_phi0 = np.cos(phi0)

    Vc_x = vx + C_l * (
            dtheta_dt * cos_psi0 * cos_theta0 - dphi_dt * (cos_psi0 * sin_theta0 * sin_phi0 - sin_psi0 * cos_phi0))
    Vc_y = vy + C_l * (
            dtheta_dt * sin_psi0 * cos_theta0 - dphi_dt * (sin_psi0 * sin_theta0 * sin_phi0 + cos_psi0 * cos_phi0))

    # 计算落点坐标
    # Calculate the impact coordinates
    x = vx * Delta_t + Vc_x * T3 + y0 * (np.tan(theta0) * cos_psi0 + np.tan(phi0) * sin_psi0) + y0 * np.tan(EFP_x)
    y = vy * Delta_t + Vc_y * T3 + y0 * (np.tan(theta0) * sin_psi0 - np.tan(phi0) * cos_psi0) + y0 * np.tan(EFP_y)

    # 计算到目标中心的欧氏距离
    # Calculate the Euclidean distance to the target center
    distance = np.sqrt(x ** 2 + y ** 2)
    return distance


# 蒙特卡洛仿真函数
# Monte Carlo Simulation Function
def monte_carlo_simulation():
    """
    执行蒙特卡洛仿真计算EFP落点分布
    Perform Monte Carlo simulation to calculate EFP impact distribution

    返回:
    x_c: numpy数组，形状为(n_samples,)，x方向落点坐标
    y_c: numpy数组，形状为(n_samples,)，y方向落点坐标
    x_c: numpy array with shape (n_samples,), impact coordinates in x direction
    y_c: numpy array with shape (n_samples,), impact coordinates in y direction
    """
    np.random.seed(42)  # 设置随机种子以确保结果可复现 Set random seed for reproducibility
    x_c = np.zeros(num_simulations)
    y_c = np.zeros(num_simulations)

    for i in range(num_simulations):
        # 随机采样参数
        # Randomly sample parameters
        vx = np.random.normal(vx_init, sigma_vx)
        vy = np.random.normal(vy_init, sigma_vy)
        T1_sim = np.random.normal(T1, sigma_T1)
        theta0 = np.random.normal(theta_init, sigma_theta)
        phi0 = np.random.normal(phi_init, sigma_phi)
        psi0 = np.random.normal(psi_init, sigma_psi)
        dtheta_dt = np.random.normal(0, sigma_dtheta_dt)
        dphi_dt = np.random.normal(0, sigma_dphi_dt)
        dpsi_dt = np.random.normal(0, sigma_dpsi_dt)

        T3 = y0 / (np.cos(theta0) * Vp)
        Delta_t = T1_sim + T2

        cos_psi0 = np.cos(psi0)
        sin_psi0 = np.sin(psi0)
        sin_theta0 = np.sin(theta0)
        sin_phi0 = np.sin(phi0)
        cos_phi0 = np.cos(phi0)

        # 计算牵连速度
        # Calculate the convective velocity
        Vc_x = vx + C_l * (dtheta_dt * cos_psi0 * np.cos(theta0) - dphi_dt * (
                cos_psi0 * sin_theta0 * sin_phi0 - sin_psi0 * cos_phi0))
        Vc_y = vy + C_l * (dtheta_dt * sin_psi0 * np.cos(theta0) - dphi_dt * (
                sin_psi0 * sin_theta0 * sin_phi0 + cos_psi0 * cos_phi0))

        # 随机采样EFP误差
        # Randomly sample EFP errors
        EFP_error_x = np.random.normal(0, sigma_EFP)
        EFP_error_y = np.random.normal(0, sigma_EFP)

        # 计算落点坐标
        # Calculate the impact coordinates
        x_c[i] = vx * Delta_t + Vc_x * T3 + y0 * (np.tan(theta0) * cos_psi0 + np.tan(phi0) * sin_psi0) + y0 * np.tan(
            EFP_error_x)
        y_c[i] = vy * Delta_t + Vc_y * T3 + y0 * (np.tan(theta0) * sin_psi0 - np.tan(phi0) * cos_psi0) + y0 * np.tan(
            EFP_error_y)

    return x_c, y_c


# 计算命中概率
# Calculate Hit Probability
def calculate_hit_probability(x_c, y_c):
    """
    计算EFP命中目标的概率
    Calculate the probability of EFP hitting the target

    参数:
    x_c: numpy数组，形状为(n_samples,)，x方向落点坐标
    y_c: numpy数组，形状为(n_samples,)，y方向落点坐标

    返回:
    hit_probability: float，命中概率
    """
    hit_count = np.sum((np.abs(x_c) <= target_width / 2) & (np.abs(y_c) <= target_height / 2))
    hit_probability = hit_count / num_simulations
    return hit_probability


# 计算95%概率圆半径
# Calculate 95% Probability Circle Radius
def calculate_95_percent_circle_radius(x_c, y_c):
    """
    计算EFP落点分布的95%概率圆半径
    Calculate the radius of the 95% probability circle for EFP impact distribution

    参数:
    x_c: numpy数组，形状为(n_samples,)，x方向落点坐标
    y_c: numpy数组，形状为(n_samples,)，y方向落点坐标

    返回:
    radius: float，95%概率圆半径
    """
    radius_x = np.percentile(x_c, 97.5) - np.percentile(x_c, 2.5)
    radius_y = np.percentile(y_c, 97.5) - np.percentile(y_c, 2.5)
    radius = max(radius_x, radius_y) / 2
    return radius    