import matplotlib
import numpy as np
import pandas as pd
from keras.models import load_model
import joblib
import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from tqdm import tqdm
from constant import *
import warnings
warnings.filterwarnings('ignore')
matplotlib.use('TkAgg')


def create_output_folder():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"output_results_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def load_hybrid_model(model_dir='model'):
    gru_model = load_model(os.path.join(model_dir, 'gru_model.h5'))

    xgb_model = joblib.load(os.path.join(model_dir, 'xgb_model.pkl'))

    meta_model = joblib.load(os.path.join(model_dir, 'meta_model.pkl'))

    feature_selector = joblib.load(os.path.join(model_dir, 'feature_selector.pkl'))

    scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))

    imputer = joblib.load(os.path.join(model_dir, 'imputer.pkl'))

    with open(os.path.join(model_dir, 'model_config.json'), 'r') as f:
        model_config = json.load(f)

    return {
        'gru_model': gru_model,
        'xgb_model': xgb_model,
        'meta_model': meta_model,
        'feature_selector': feature_selector,
        'scaler': scaler,
        'imputer': imputer,
        'config': model_config
    }


def predict_with_hybrid_model(models, new_data):
    required_features = models['config']['feature_names']
    new_data = new_data[required_features]

    new_data_imputed = pd.DataFrame(
        models['imputer'].transform(new_data),
        columns=new_data.columns
    )

    scaled_data = models['scaler'].transform(new_data_imputed)

    selected_features = models['feature_selector'].transform(scaled_data)

    gru_input = selected_features.reshape(selected_features.shape[0],
                                          selected_features.shape[1], 1)
    gru_proba = models['gru_model'].predict(gru_input).ravel()

    xgb_proba = models['xgb_model'].predict_proba(selected_features)[:, 1]

    meta_features = np.column_stack([gru_proba, xgb_proba])
    final_proba = models['meta_model'].predict_proba(meta_features)[:, 1]
    final_predictions = (final_proba > models['config']['threshold']).astype(int)

    return final_predictions, final_proba, gru_proba, xgb_proba


def save_visualizations(results, example_data, output_dir):
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8, 6))
    results['预测结果'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
    plt.title('预测结果分布 (0=正常, 1=欺诈)')
    plt.ylabel('')
    plt.savefig(os.path.join(output_dir, 'prediction_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    conf_counts = results['置信度评估'].value_counts()
    sns.barplot(x=conf_counts.index, y=conf_counts.values, palette="Blues_d")
    plt.title('置信度分布')
    plt.ylabel('样本数量')
    plt.savefig(os.path.join(output_dir, 'confidence_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.histplot(results['最终预测概率'], bins=20, kde=True, color='skyblue')
    plt.title('预测概率分布')
    plt.xlabel('预测概率')
    plt.savefig(os.path.join(output_dir, 'probability_distribution.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.scatter(results['GRU模型概率'], results['XGBoost模型概率'],
                c=results['最终预测概率'], cmap='coolwarm', alpha=0.6)
    plt.colorbar(label='最终预测概率')
    plt.plot([0, 1], [0, 1], 'k--', alpha=0.3)
    plt.xlabel('GRU模型概率')
    plt.ylabel('XGBoost模型概率')
    plt.title('基模型概率对比')
    plt.savefig(os.path.join(output_dir, 'model_comparison.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    high_risk = results[(results['预测结果'] == 1) & (results['置信度评估'] == '高置信度')]
    if len(high_risk) > 0:
        example_data_high_risk = example_data.iloc[high_risk.index]
        top_features = example_data_high_risk.mean().sort_values(ascending=False)[:3]
        sns.barplot(x=top_features.values, y=top_features.index, palette="viridis")
        plt.title('高风险样本TOP3特征均值')
    else:
        plt.text(0.5, 0.5, '无高风险样本', ha='center', va='center')
        plt.axis('off')
    plt.savefig(os.path.join(output_dir, 'high_risk_features.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x=results['预测结果'], y=results['最终预测概率'], palette='Set2', inner=None)
    plt.title('预测概率分布')
    plt.savefig(os.path.join(output_dir, 'probability_violin_boxplot.png'),
                dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    corr_matrix = results[['GRU模型概率', 'XGBoost模型概率', '最终预测概率']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('模型概率相关性')
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(8, 6))
    pd.crosstab(results['置信度评估'], results['预测结果']).plot.bar(stacked=True, color=['lightgreen', 'salmon'])
    plt.title('置信度 vs 预测结果')
    plt.ylabel('样本数量')
    plt.savefig(os.path.join(output_dir, 'confidence_vs_prediction.png'), dpi=300, bbox_inches='tight')
    plt.close()


def generate_user_features(USER_INFO, RECORD_INFO, GEN_FEATURE=True):
    tqdm.pandas()

    # Load data
    with tqdm(total=3, desc="Loading data") as pbar:
        user_info_df = pd.read_excel(USER_INFO)[['zhdh', 'xb', '年龄']]
        pbar.update(1)
        record_info_df = pd.read_excel(RECORD_INFO)
        pbar.update(1)
        pbar.update(1)

    JYQD = record_info_df['jyqd'].unique()

    def cat2cnt(series):
        try:
            series = series.astype(str)
        except (ValueError, TypeError):
            pass

        if pd.api.types.is_numeric_dtype(series):
            series = series.astype('category')

        map_ = series.groupby(series).agg('count').to_dict()
        return series.map(map_)

    def agg_user_record_features(one_user_feature_df):
        for col in ['dfzh', 'dfhh'] + [c for c in RECORD_CAT_COLS if c != 'zydh']:
            if col in one_user_feature_df.columns:
                one_user_feature_df[col] = one_user_feature_df[col].astype(str)

        feature_dict = {
            USER_ID_COL: one_user_feature_df[USER_ID_COL].iloc[0],
            'NumRecord': len(one_user_feature_df)
        }

        num_ops = ['min', 'max', 'std', 'mean', 'median']

        for col in ['dfzh', 'dfhh']:
            feature_dict['{}_List'.format(col)] = one_user_feature_df[col].agg(list)
            feature_dict['{}_Nunique'.format(col)] = one_user_feature_df[col].nunique()
            feature_dict['{}_NuniqueDivLen'.format(col)] = one_user_feature_df[col].nunique() / len(one_user_feature_df)

        feature_dict['jdbj_InCnt'] = one_user_feature_df['jdbj'].sum()
        feature_dict['jdbj_OutCnt'] = len(one_user_feature_df) - one_user_feature_df['jdbj'].sum()
        feature_dict['jdbj_InRatio'] = one_user_feature_df['jdbj'].sum() / len(one_user_feature_df)

        for col in ['jyje', 'zhye'] + ['{}_cnt'.format(col) for col in RECORD_CAT_COLS if col != 'zydh']:
            for op in num_ops:
                feature_dict['{}_{}'.format(col, op.capitalize())] = one_user_feature_df[col].agg(op)
            feature_dict['{}_Range'.format(col)] = feature_dict['{}_Max'.format(col)] - feature_dict[
                '{}_Min'.format(col)]

        for op in num_ops:
            in_op_val = one_user_feature_df[one_user_feature_df['jdbj'] == 1]['jyje'].agg(op)
            out_op_val = one_user_feature_df[one_user_feature_df['jdbj'] == 0]['jyje'].agg(op)
            feature_dict['InMoney_{}'.format(op.capitalize())] = in_op_val
            feature_dict['OutMoney_{}'.format(op.capitalize())] = out_op_val
            feature_dict['InMoney_{}Ratio'.format(op.capitalize())] = in_op_val / (in_op_val + out_op_val + EPS)

        feature_dict['jdbj_InUserCnt'] = one_user_feature_df[one_user_feature_df['jdbj'] == 1]['dfzh'].nunique()
        feature_dict['jdbj_OutUserCnt'] = one_user_feature_df[one_user_feature_df['jdbj'] == 0]['dfzh'].nunique()
        feature_dict['jdbj_InUserRatio'] = feature_dict['jdbj_InUserCnt'] / (
                feature_dict['jdbj_InUserCnt'] + feature_dict['jdbj_OutUserCnt'] + EPS)

        feature_dict['whole_life_jy_Interval(h)'] = \
            (one_user_feature_df['jyts'].max() - one_user_feature_df['jyts'].min()).total_seconds() / 3600
        feature_dict['jy_Freq(h)'] = feature_dict['whole_life_jy_Interval(h)'] / len(one_user_feature_df)

        for op in num_ops:
            feature_dict['jyje_{}DivFreq'.format(op.capitalize())] = \
                feature_dict['jyje_{}'.format(op.capitalize())] / feature_dict['jy_Freq(h)']
            feature_dict['oneday_jytimes_{}'.format(op.capitalize())] = \
                one_user_feature_df.groupby("jyrq")['jyts'].agg('count').agg(op)
            feature_dict['jytimestampval_{}'.format(op.capitalize())] = \
                (pd.to_numeric(one_user_feature_df['jyts']) / 1e9).agg(op)

        for op in num_ops:
            feature_dict['jy_interval_{}'.format(op.capitalize())] = \
                one_user_feature_df['jyts'].diff(1).dt.total_seconds().agg(op)
            feature_dict['jy_day_{}'.format(op.capitalize())] = one_user_feature_df['jyts'].dt.day.agg(op)
            feature_dict['jy_weekday_{}'.format(op.capitalize())] = one_user_feature_df['jyts'].dt.dayofweek.agg(op)
            feature_dict['jy_hour_{}'.format(op.capitalize())] = one_user_feature_df['jyts'].dt.hour.agg(op)
            feature_dict['jy_monthstart_{}'.format(op.capitalize())] = one_user_feature_df[
                'jyts'].dt.is_month_start.agg(op)
            feature_dict['jy_monthend_{}'.format(op.capitalize())] = one_user_feature_df['jyts'].dt.is_month_end.agg(op)
            feature_dict['jy_wkend_{}'.format(op.capitalize())] = (one_user_feature_df['jyts'].dt.dayofweek // 6).agg(
                op)

        for ts in ['day', 'weekday', 'hour']:
            feature_dict['jy_{}_nunique'.format(ts)] = getattr(one_user_feature_df['jyts'].dt, ts).nunique()

        feature_dict['jyts_Min'] = one_user_feature_df['jyts'].min()
        feature_dict['jyts_Max'] = one_user_feature_df['jyts'].max()

        for col in ['dfzh', 'dfhh']:
            for op in num_ops:
                feature_dict['{}_GroupCount_{}'.format(col, op.capitalize())] = \
                    one_user_feature_df.groupby(col)[col].agg('count').agg(op)

        if 'jyqd' in one_user_feature_df.columns:
            if pd.api.types.is_numeric_dtype(one_user_feature_df['jyqd']):
                for op in num_ops:
                    feature_dict['jyqd_{}'.format(op.capitalize())] = one_user_feature_df['jyqd'].agg(op)
                feature_dict['jyqd_nunique'] = one_user_feature_df['jyqd'].nunique()
            else:
                feature_dict['jyqd_nunique'] = one_user_feature_df['jyqd'].nunique()

        for op in num_ops:
            feature_dict['dfmccd_{}'.format(op.capitalize())] = one_user_feature_df['dfmccd'].agg(op)

        return pd.DataFrame([feature_dict])

    def delete_list_cols(df):
        new_df = df.copy()
        is_list = new_df.columns.str.endswith('_List')
        list_cols = new_df.columns[is_list].to_list()
        new_df = new_df.drop(list_cols, axis=1)
        return new_df

    def process_combined_feature(df):
        df['age'] = df['年龄']
        return df

    # Merge data
    with tqdm(total=3, desc="Merging data") as pbar:
        all_user_ids = user_info_df['zhdh'].unique()
        user_record_df = record_info_df[record_info_df['zhdh'].isin(all_user_ids)]
        pbar.update(1)

        user_record_df['jyts'] = pd.to_datetime(
            user_record_df['jyrq'].astype(str) + ' ' + user_record_df['jysj'].astype(str),
            errors='coerce'
        )
        pbar.update(1)
        pbar.set_postfix({"Records": len(user_record_df), "Users": user_record_df['zhdh'].nunique()})
        pbar.update(1)

    # Process count features
    with tqdm(total=len([c for c in RECORD_CAT_COLS if c != 'zydh']),
              desc="Processing count features") as pbar:
        for col in [c for c in RECORD_CAT_COLS if c != 'zydh']:
            if col in user_record_df.columns:
                ss = cat2cnt(user_record_df[col])
                user_record_df['{}_cnt'.format(col)] = ss
            pbar.update(1)
            pbar.set_postfix({"current_column": col})

    if not GEN_FEATURE and os.path.exists(SAVE_DIR / "all_user_record_and_static_info_df.csv"):
        all_user_record_and_static_info_df = pd.read_csv(SAVE_DIR / "all_user_record_and_static_info_df.csv")
    else:
        with tqdm(total=3, desc="Feature engineering") as pbar:
            user_agg_records = []
            for zhdh, group in tqdm(user_record_df.groupby(USER_ID_COL),
                                    desc="Processing users",
                                    leave=False):
                user_agg_records.append(agg_user_record_features(group))

            user_agg_record_df = pd.concat(user_agg_records, ignore_index=True)
            pbar.update(1)

            user_agg_record_df = delete_list_cols(user_agg_record_df)
            pbar.update(1)

            all_user_record_and_static_info_df = user_agg_record_df.merge(
                user_info_df, on='zhdh', how='left')
            all_user_record_and_static_info_df = process_combined_feature(
                all_user_record_and_static_info_df)
            pbar.update(1)

    print("\nFeature extraction completed successfully for all users!")
    return all_user_record_and_static_info_df

def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)
    return path

def main():
    all_user_record_and_static_info_df = generate_user_features(USER_INFO, RECORD_INFO)
    model_components = load_hybrid_model()

    example_data = all_user_record_and_static_info_df

    example_data = example_data.select_dtypes(include=[np.number])

    required_features = model_components['config']['feature_names']
    missing_features = set(required_features) - set(example_data.columns)
    if missing_features:
        raise ValueError(f"缺少必要特征: {missing_features}")

    predictions, final_proba, gru_proba, xgb_proba = predict_with_hybrid_model(model_components, example_data)

    results = pd.DataFrame({
        '预测结果': predictions,
        '最终预测概率': final_proba,
        'GRU模型概率': gru_proba,
        'XGBoost模型概率': xgb_proba,
        '置信度评估': np.where(final_proba > 0.7, '高置信度',
                          np.where(final_proba > 0.3, '中置信度', '低置信度'))
    })

    output_dir = ensure_directory_exists(r'E:\电脑桌面\模型\image')
    output_file = os.path.join(output_dir, 'prediction_results_with_confidence.csv')
    results.to_csv(output_file, index=False, encoding='utf-8-sig')

    print(f"预测结果已保存到: {os.path.abspath(output_file)}")
    print("\n预测结果详情:")
    print(results.head())

    print("\n置信度分布统计:")
    print(results['置信度评估'].value_counts())

    high_risk = results[(results['预测结果'] == 1) & (results['置信度评估'] == '高置信度')]
    print(f"\n发现 {len(high_risk)} 个高风险样本(预测为欺诈且高置信度):")
    print(high_risk)

    save_visualizations(results, example_data, output_dir)

    print("\n可视化分析图表已保存到文件夹:")
    print(f"{os.path.abspath(output_dir)}")
    print("包含以下文件:")
    print("1. prediction_distribution.png - 预测结果分布")
    print("2. confidence_distribution.png - 置信度分布")
    print("3. probability_distribution.png - 预测概率分布")
    print("4. model_comparison.png - 基模型概率对比")
    print("5. high_risk_features.png - 高风险样本特征")
    print("6. probability_boxplot.png - 预测概率箱线图")
    print("7. correlation_heatmap.png - 模型概率相关性")
    print("8. confidence_vs_prediction.png - 置信度与预测结果关系")

if __name__ == "__main__":
    main()