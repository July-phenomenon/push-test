from data_process import load_and_split_data, plot_data_analysis
from models import train_models
from metrics_eval import evaluate_and_generate_table
from visualization import plot_model_results

def main():
    print("="*50)
    print("开始复刻：基于机器学习的盐水甲烷水合物形成条件预测")
    print("="*50)
    
    # 1. 数据加载与分析 (复现 Fig 1)
    print("\n[1/4] 正在加载数据并绘制数据分布图...")
    X_train, X_test, y_train, y_test, df = load_and_split_data()
    plot_data_analysis(df)
    
    # 2. 模型训练
    print("\n[2/4] 正在训练5大机器学习模型 (MLR, k-NN, SVR, RF, GBR)...")
    models, scaler = train_models(X_train, y_train)
    
    # 3. 评估指标与表格生成 (复现 Table 2)
    print("\n[3/4] 正在计算评估指标并生成 Table 2...")
    df_results, predictions = evaluate_and_generate_table(models, scaler, X_train, y_train, X_test, y_test)
    print("\n论文 Table 2 结果展示：")
    print(df_results[['Model', 'Test_R2', 'Test_RMSE', 'Test_AARD%']])
    
    # 4. 图表生成 (复现 Fig 2 到 Fig 6)
    print("\n[4/4] 正在生成预测图与残差图 (Fig 2 - Fig 6)...")
    model_mapping = {
        'MLR': 2,
        'k-NN': 3,
        'SVR': 4,
        'RF': 5,
        'GBR': 6
    }
    
    for model_name, fig_num in model_mapping.items():
        y_tr_pred = predictions[model_name]['train_pred']
        y_te_pred = predictions[model_name]['test_pred']
        plot_model_results(model_name, y_train, y_tr_pred, y_test, y_te_pred, fig_num)
        
    print("\n" + "="*50)
    print("复刻完成！所有图表和表格已保存在 d:\\chemistryfuke\\输出\\ 目录下。")
    print("="*50)

if __name__ == "__main__":
    main()