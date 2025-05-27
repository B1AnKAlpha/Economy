import os
import webbrowser

#gtk_path = r"E:\Economy\Download\Project\final"
#gtk_path = r"E:\GTK\GTK3-RuntimeWin64\bin"
#os.environ["PATH"] = gtk_path + os.pathsep + os.environ["PATH"]
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
import os
from jinja2 import Environment, FileSystemLoader
import pdfkit


warnings.filterwarnings('ignore')
matplotlib.use('Agg')


def create_output_folder():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"output_results_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def load_hybrid_model(model_dir='./final/model'):
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
    nan_cols = new_data.columns[new_data.isna().any()].tolist()
    posinf_cols = new_data.columns[np.isposinf(new_data).any()].tolist()
    neginf_cols = new_data.columns[np.isneginf(new_data).any()].tolist()

    # 打印详细信息
    print("是否包含 NaN：", bool(nan_cols), "列名：", nan_cols)
    print("是否包含正无穷：", bool(posinf_cols), "列名：", posinf_cols)
    print("是否包含负无穷：", bool(neginf_cols), "列名：", neginf_cols)


    if new_data.isna().any().any():
        print("有缺失值，正在填补...")
        new_data.replace([np.inf, -np.inf], np.nan, inplace=True)
        new_data.fillna(0, inplace=True)  # 或者使用其他填补策略

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

import os
import pandas as pd
import pdfkit

import pandas as pd
import os
import pdfkit
import pymysql
from datetime import datetime

import pandas as pd
import os
import pdfkit
import pymysql
from datetime import datetime

import pandas as pd
import os
import pdfkit
import pymysql
from datetime import datetime

import pandas as pd
import os
import pdfkit
import pymysql
from datetime import datetime

import pandas as pd
import os
import pdfkit
import pymysql
from datetime import datetime


def export_results_to_pdf(time_str,output_dir, user_info_path, prediction_csv_path, wkhtmltopdf_path=None,):
    user_info_df = pd.read_excel(user_info_path)
    prediction_df = pd.read_csv(prediction_csv_path)

    try:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="yupeihao05ab",
            database="locallog",
            charset="utf8mb4"
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT predictModelVersion FROM localmodel;")
            model_version_row = cursor.fetchone()
            model_version = model_version_row[0] if model_version_row else "未知"

            cursor.execute("SELECT version FROM localparameter;")
            param_version_row = cursor.fetchone()
            param_version = param_version_row[0] if param_version_row else "未知"
        conn.close()
    except Exception as e:
        print("❌ 数据库查询失败:", e)
        model_version = "未知"
        param_version = "未知"

    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_info_df = user_info_df.rename(columns={
        user_info_df.columns[0]: "转账账户",
        user_info_df.columns[1]: "性别",
        user_info_df.columns[2]: "年龄"
    })
    if "性别" in user_info_df.columns:
        # 定义映射关系
        gender_map = {1: "男", 0: "女", "1": "男", "0": "女"}

        # 使用 .map()进行转换，对于不在映射中的值，可以保留原样或设为特定值
        # .get(x, x) 会在找不到key时返回x本身（原值）
        # 或者使用 .get(x, '未知') 如果希望未映射的值显示为'未知'
        user_info_df["性别"] = user_info_df["性别"].map(lambda x: gender_map.get(x, str(x)))

        # 更简洁的写法，如果确定值只有 0, 1 (数字或字符串):
        # user_info_df["性别"] = user_info_df["性别"].astype(str).map({"1": "男", "0": "女"}).fillna(user_info_df["性别"])
        # 或者，如果确定是数字 0 和 1：
        # user_info_df["性别"] = user_info_df["性别"].map({1: "男", 0: "女"})
    prediction_col_name = None
    # 尝试自动识别列名，你可以根据实际CSV中的列名调整这个列表
    possible_pred_cols = ['Prediction', '预测结果',
                          prediction_df.columns[1] if len(prediction_df.columns) > 1 else None]
    for col in possible_pred_cols:
        if col and col in prediction_df.columns:
            prediction_col_name = col
            break

    if prediction_col_name:
        print(f"找到预测结果列: '{prediction_col_name}' 进行转换")
        prediction_map = {1: "欺诈账户", 0: "非欺诈账户", "1": "欺诈账户", "0": "非欺诈账户"}

        # 确保在映射前，数据是正确的类型（例如，如果它们是字符串'1.0'，先转为数字或处理）
        # 为了安全，可以先尝试转为整数，如果失败则按原样处理
        def safe_map_prediction(x):
            try:
                # 尝试将 x 转换为整数（如果它是浮点数如 1.0，或字符串如 "1"）
                val = int(float(str(x)))  # str(x) to handle non-string types first
                return prediction_map.get(val, str(x))
            except (ValueError, TypeError):
                return prediction_map.get(x, str(x))  # Fallback for direct string match or unconvertible

        prediction_df[prediction_col_name] = prediction_df[prediction_col_name].apply(safe_map_prediction)
    else:
        print(f"⚠️ 警告：未能自动识别预测结果列。将使用原始值。检查列名: {prediction_df.columns}")

    # 2. 置信度高亮 (假设列名为 'Confidence' 或 '置信度'，并且内容是文本："低置信度", "中置信度", "高置信度")
    confidence_col_name = None
    # 尝试自动识别列名
    possible_conf_cols = ['Confidence', '置信度评估', prediction_df.columns[2] if len(prediction_df.columns) > 2 else None]
    for col in possible_conf_cols:
        if col and col in prediction_df.columns:
            confidence_col_name = col
            break

    # 生成带样式的HTML表格，而不是修改DataFrame再to_html
    # 这样可以更灵活地控制行样式
    user_info_html = user_info_df.to_html(index=False, classes='data-table user-info-table', border=0)
    prediction_html = prediction_df.to_html(index=False, classes='data-table', border=0)
    if confidence_col_name:
        print(f"找到置信度列: '{confidence_col_name}' 用于高亮")

        def get_row_style(row_series):
            confidence_value = str(row_series[confidence_col_name]).strip()  # Ensure string and remove whitespace
            if "高置信度" in confidence_value:  # Use "in" for flexibility if there are extra spaces
                return 'style="background-color: #FFC0CB;"'  # Pink - High confidence, very bright
            elif "中置信度" in confidence_value:
                return 'style="background-color: #FFFF99;"'  # Light Yellow - Medium confidence
            return ''  # Default, no style

        # Manually build the HTML table for predictions to include row styles
        html_rows = []
        # Header row
        header_html = "<tr>" + "".join([f"<th>{col_name}</th>" for col_name in prediction_df.columns]) + "</tr>"
        html_rows.append(header_html)

        # Data rows
        for index, row in prediction_df.iterrows():
            style = get_row_style(row)
            row_html = f"<tr {style}>" + "".join([f"<td>{value}</td>" for value in row]) + "</tr>"
            html_rows.append(row_html)

        prediction_html = f'<table class="data-table"><tbody>{"".join(html_rows)}</tbody></table>'
    else:
        print(f"⚠️ 警告：未能自动识别置信度列 '{possible_conf_cols}'。预测结果表将不进行置信度高亮。")
        # Fallback to default HTML generation if confidence column not found
        prediction_html = prediction_df.to_html(index=False, classes='data-table', border=0, na_rep='-')


    img_infos = [
        ("prediction_distribution.png", "预测结果分布图"),
        ("confidence_distribution.png", "样本置信度分布"),
        ("probability_distribution.png", "预测概率分布图"),
        ("model_comparison.png", "GRU与XGBoost模型概率对比"),
        ("high_risk_features.png", "高风险样本 TOP3 特征均值"),
        ("probability_violin_boxplot.png", "预测概率的箱线图与小提琴图"),
        ("correlation_heatmap.png", "模型概率之间的相关性热力图"),
        ("confidence_vs_prediction.png", "置信度与预测标签的关系"),
    ]

    img_table_rows = ""
    for i in range(0, len(img_infos), 2):
        def build_img_cell(img_name, desc):
            path = os.path.join(output_dir, img_name)
            if os.path.exists(path):
                abs_path = os.path.abspath(path).replace("\\", "/")
                return f"""
                    <div class="chart-card">
                        <h3>{desc}</h3>
                        <img src="file:///{abs_path}" alt="{desc}">
                    </div>"""
            return ""

        left_html = build_img_cell(*img_infos[i])
        right_html = build_img_cell(*img_infos[i + 1]) if i + 1 < len(img_infos) else ""

        img_table_rows += f"""
        <tr>
            <td class="chart-td">{left_html}</td>
            <td class="chart-td">{right_html}</td>
        </tr>"""

    background_image_path_rel = "./final/back.jpg"
    background_image_path_abs = ""
    if os.path.exists(background_image_path_rel):
        background_image_path_abs = os.path.abspath(background_image_path_rel).replace("\\", "/")
    else:
        print(f"⚠️ 警告：背景图片 '{background_image_path_rel}' 不存在。")

    body_background_style = ""
    if background_image_path_abs:
        body_background_style = f"""
            background-image: url('file:///{background_image_path_abs}');
            background-repeat: no-repeat; /* 确保背景图不重复平铺 */
            background-position: center center;
            background-size: 100% 100%; /* 变形填充整个body区域 */
            /* background-attachment: scroll;  是默认值，无需显式设置 */
        """
    else:
        body_background_style = "background-color: #f0f0f0;"  # 备用背景色

    desired_top_spacing = "25mm"  # 边距问题已解决，保持这个值

    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
        @page {{
            size: A4;
            margin: 0mm; /* 页面本身无边距 */
        }}
        html {{ /* html元素也设置为100%高宽，并应用 print-color-adjust */
            font-family: 'Microsoft YaHei', 'SimHei', Arial, sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%; 
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
        }}
        body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%; /* 关键：尝试让body在wkhtmltopdf的每一页都填充100%高度 */
            box-sizing: border-box;
            {body_background_style} /* 背景应用到body */
            -webkit-print-color-adjust: exact !important; /* 强制打印背景 */
        }}
        .top-spacer {{
            height: {desired_top_spacing};
            width: 100%;
        }}
        .page-content {{
            margin-top: 0mm; /* 由.top-spacer控制实际内容顶部位置 */
            margin-bottom: 12mm;
            margin-left: 15mm;
            margin-right: 15mm;
            padding: 1px; /* 防止子元素的margin collapsing */
            box-sizing: border-box;
            position: relative; /* 确保z-index生效 */
            z-index: 1; /* 确保内容在背景之上 */
            /* 如果内容区域本身需要一个不透明背景（比如白色），可以取消注释下一行 */
            /* background-color: white; */
        }}
        h1, h2 {{
            text-align: center;
            color: #2c3e50;
        }}
        h1 {{
            font-size: 28px;
            margin-top: 0; 
            padding-top: 10px;
        }}
        .subtitle {{
            font-size: 16px;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
            color: #555;
        }}
        h2 {{
            font-size: 22px;
            margin-top: 40px;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            font-size: 14px;
            background-color: #fff; /* 表格使用白色背景确保可读性 */
        }}
        .data-table th, .data-table td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
        }}
        .user-info-table th {{
            background-color: #2980b9;
            color: white;
        }}
        .data-table th {{ 
            background-color: #3498db;
            color: white;
        }}
        .img-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 15px 30px; 
            margin-bottom: 40px;
        }}
        .chart-td {{
            width: 50%;
            vertical-align: top;
            padding:0; 
        }}
        .chart-card {{
            background-color: #fff; 
            border-radius: 8px;
            padding: 12px 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            text-align: center;
            height: 340px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            overflow: hidden;
        }}
        .chart-card h3 {{
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 12px;
            color: #2c3e50;
            height: 44px; 
            line-height: 22px;
            flex-shrink: 0; 
        }}
        .chart-card img {{
            max-width: 100%;
            max-height: calc(100% - 44px - 12px - 2px); /* h3 + margin + border */
            object-fit: contain;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin: 0 auto; 
            flex-grow: 1; 
            display: block;
        }}
        </style>
    </head>
    <body>
        <div class="page-content">
            <div class="top-spacer"></div>
            <h1>金融欺诈检测分析报告</h1>
            <div class="subtitle">
                当前使用模型版本：{model_version}    
                当前使用参数版本：{param_version}    
                生成报告时间：{report_time}
            </div>
            <h2>一、用户信息</h2>
            {user_info_html}
            <h2>二、预测结果</h2>
            {prediction_html}
            <h2>三、分析图表</h2>
            <table class="img-table">
                {img_table_rows}
            </table>
        </div>
    </body>
    </html>
    """

    html_path = os.path.join(output_dir, "report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    pdfname = time_str+".pdf"
    pdf_path = os.path.join(output_dir, pdfname)

    try:
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path) if wkhtmltopdf_path else None
        options = {
            'encoding': 'UTF-8',
            'page-size': 'A4',
            'margin-top': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
            'margin-right': '0mm',
            'enable-local-file-access': None,
            'print-media-type': None,  # 确保使用屏幕样式
            'background': None,  # 明确启用背景打印
            '--disable-smart-shrinking': None,  # 尝试禁用wkhtmltopdf的智能缩放
            # 'zoom': '1', # 有时明确设置缩放为1可以避免一些奇怪的渲染问题
        }
        pdfkit.from_file(html_path, pdf_path, configuration=config, options=options)
        print(f"✅ PDF报告已生成：{pdf_path}")
        webbrowser.open(pdf_path)
    except Exception as e:
        print("❌ PDF生成失败，请检查 wkhtmltopdf 是否正确安装或配置，并查看HTML文件是否有渲染问题。", e)
        print(f"HTML文件已保存在: {html_path}")

    # return pdf_path # 如果需要在函数外部使用路径，可以取消注释







def main():
    requiretime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global time
    global timestr
    time = requiretime
    if isinstance(requiretime, datetime):
        requiretime = requiretime.strftime("%Y-%m-%d_%H-%M-%S")  # 先格式化，再做文件名替换
        # 若已经是字符串，确保替换非法文件名字符
    time_str = requiretime.replace(":", "-").replace(" ", "_")
    print(time)
    print("time_str", time_str)
    with open("./final/user.txt", "r", encoding="utf-8") as f:
        username = f.read().strip()
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="yupeihao05ab",
        database="locallog",
        charset="utf8mb4"
    )

    # 创建游标
    cursor = conn.cursor()

    sql = "INSERT INTO localpdflog (time, username) VALUES (%s, %s)"

    # 执行插入
    cursor.execute(sql, (time, username))

    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

    print("插入成功：", time, username)

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

    output_dir = ensure_directory_exists('./final/result')
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

    export_results_to_pdf(time_str,output_dir, USER_INFO, output_file)

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