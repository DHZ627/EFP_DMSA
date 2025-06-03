# EFP散布分析程序 EFP Dispersion Analysis Program

## 项目简介 Project Overview

本程序用于分析爆炸成型弹丸(EFP)的弹道散布特性，通过蒙特卡洛模拟和Sobol全局敏感性分析评估各种误差因素对EFP命中精度的影响。程序可以计算命中概率、95%概率圆半径，并可视化落点分布和敏感性分析结果。
This program is designed to analyze the dispersion characteristics of Explosively Formed Penetrators (EFPs). It uses Monte Carlo simulation and Sobol global sensitivity analysis to evaluate the impact of various error factors on EFP hit accuracy. The program can calculate hit probability, 95% probability circle radius, and visualize impact distributions and sensitivity analysis results.


## 环境配置 Environment Configuration

### 依赖库 Dependencies
本项目需要以下 Python 库及其对应版本（建议使用指定版本避免兼容性问题）：
The project requires the following Python libraries and versions (recommended to avoid compatibility issues):

| 库名 Library| 版本要求 Version Required| 说明 Description |
|---------------|----------------|--------------------------|
| `numpy`       | >= 1.21.0      | 科学计算基础库 Fundamental scientific computing library           |
| `matplotlib`  | >= 3.4.0       | 数据可视化 Data visualization         |
| `scipy`       | >= 1.7.0       | 科学计算工具包 Scientific computing tools          |
| `SALib`       | == 1.4.6       | 敏感性分析库（需固定版本） Sensitivity analysis library (fixed version required)|
| `pandas`      | >= 1.3.0       | 数据处理与分析 Data processing and analysis|

### 环境搭建步骤 Setup Steps

#### 方法一：使用 `pip` 安装（推荐） Method 1: Install via `pip` (Recommended)

1. 创建并激活 Python 虚拟环境（可选，但建议使用）：Create and activate a Python virtual environment (optional but recommended):
   ```bash
   # Linux/macOS
   python -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```
2. 安装依赖库： Install dependencies:
   ```bash
   pip install numpy matplotlib scipy SALib==1.4.6 pandas
   ```

#### 方法二：使用 `requirements.txt` 文件 Method 2: Use `requirements.txt`
1. 创建 `requirements.txt` 文件（内容如下）： Create a `requirements.txt` file with the following content:
   ```txt
   numpy>=1.21.0
   matplotlib>=3.4.0
   scipy>=1.7.0
   SALib==1.4.6
   pandas>=1.3.0
   ```
2. 安装依赖： Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 版本说明 Version Notes

- `SALib==1.4.6` 是经过测试的兼容版本，避免使用 `1.5.0+` 版本（可能包含弃用接口）。`SALib==1.4.6` is the tested compatible version. Avoid using `1.5.0+` (may include deprecated interfaces).

- 若遇到兼容性警告，可尝试升级 `pandas` 或添加警告过滤（见代码注释）。If compatibility warnings occur, try upgrading `pandas` or adding warning filters (see comments in the code).


## 功能特点 Features

- 蒙特卡洛模拟EFP落点分布 Monte Carlo simulation of EFP impact distribution
- 计算命中概率和95%概率圆半径 Calculation of hit probability and 95% probability circle radius
- Sobol全局敏感性分析 Sobol global sensitivity analysis
- 可视化EFP落点分布和参数敏感性 Visualization of EFP impact distribution and parameter sensitivity

## 安装依赖pip install numpy matplotlib scipy SALib pandas Installation Requirementspip install numpy matplotlib scipy SALib pandas

使用方法python main.py程序将自动执行蒙特卡洛模拟和敏感性分析，并生成相应的图表和结果文件。
Usagepython main.pyThe program will automatically execute the Monte Carlo simulation and sensitivity analysis, then generate corresponding charts and result files.

## 项目结构 Project Structureefp/
```plaintext
EFP_DMSA/
├──main.py                    # 主程序入口 Main program entry
├── parameters.py             # 参数配置模块 Parameter configuration module
├── model.py                  # 模型计算模块 Model calculation module
├── visualization.py          # 可视化模块 Visualization module
├── impact_distribution.png   # 落点分布图 Impact distribution chart
├── sensitivity_analysis.png  # 敏感性分析图 Sensitivity analysis chart
├── global_sobol.csv          # 敏感性分析结果 Sensitivity analysis results
└── README.md                 # 项目说明文档 Project documentation
```
## 结果说明 Results Explanation
- `impact_distribution.png`: EFP落点分布和目标区域可视化 Visualization of EFP impact distribution and target area
- `sensitivity_analysis.png`: 参数敏感性分析结果可视化 Visualization of parameter sensitivity analysis results
- `global_sobol.csv`: 详细的敏感性分析数据 Detailed sensitivity analysis data

## 贡献 Contributions
欢迎对本项目提出建议或贡献代码。如需帮助，请联系项目维护者。
Suggestions and code contributions are welcome. Please contact the project maintainer for assistance.





    
