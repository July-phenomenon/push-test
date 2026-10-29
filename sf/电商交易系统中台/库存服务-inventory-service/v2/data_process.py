import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from config import DATA_PATH, FIG_DIR, FEATURES, TARGET, STATUS_COL

# 设置绘图字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False

def load_and_split_data():
    """读取数据并根据Status列划分为训练集和测试集"""
    df = pd.read_excel(DATA_PATH)
    
    train_df = df[df[STATUS_COL] == 'Train']
    test_df = df[df[STATUS_COL] == 'Test']
    
    X_train = train_df[FEATURES].values
    y_train = train_df[TARGET].values
    X_test = test_df[FEATURES].values
    y_test = test_df[TARGET].values
    
    return X_train, X_test, y_train, y_test, df

def plot_data_analysis(df):
    """复现论文 Fig. 1 (a) 相关性矩阵 和 Fig. 1 (b) 数据分布"""
    # 提取需要的列
    cols = FEATURES + [TARGET]
    data = df[cols]
    
    # Fig 1(a): 相关性矩阵热力图
    plt.figure(figsize=(10, 8))
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
    plt.title("Fig. 1 (a) Database variables correlation matrix")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "Fig_1a_Correlation_Matrix.png"), dpi=300)
    plt.close()
    
    # Fig 1(b): 特征分布及散点图 (Pairplot)
    g = sns.pairplot(data, diag_kind='hist', plot_kws={'alpha':0.6, 's':15, 'color': 'black'},
                     diag_kws={'color': 'gray'})
    g.fig.suptitle("Fig. 1 (b) Histograms and scatter plots of database variables", y=1.02)
    plt.savefig(os.path.join(FIG_DIR, "Fig_1b_Scatter_Histograms.png"), dpi=300)
    plt.close()
    print("数据分析图表 (Fig 1) 已生成！")