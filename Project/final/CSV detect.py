import pandas as pd
import sys
import os  # Added for os.path.isfile, os.makedirs, os.path.dirname


# --- Helper function to append DataFrame to an Excel file ---
def append_df_to_excel(filename, df_to_append, sheet_name='Sheet1', index=False, **to_excel_kwargs):
    """
    Append a DataFrame to an existing Excel file or create a new file.
    Handles deduplication for static data based on 'zhdh'.

    Args:
        filename (str): Path to the Excel file.
        df_to_append (pd.DataFrame): DataFrame to append.
        sheet_name (str): Name of the Excel sheet.
        index (bool): Whether to write DataFrame index.
        **to_excel_kwargs: Additional arguments to pass to df.to_excel().
    """
    if df_to_append is None or df_to_append.empty:
        print(f"⚠️ 要追加到 '{filename}' 的DataFrame为空，操作已跳过。")
        return

    # Ensure the directory exists
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):  # Check if output_dir is not empty string
        os.makedirs(output_dir, exist_ok=True)
        print(f"已创建目录: {output_dir}")

    if not os.path.isfile(filename):
        print(f"文件 '{filename}' 不存在，将创建新文件。")
        df_to_append.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
        print(f"数据已写入新文件 '{filename}'。")
    else:
        try:
            print(f"文件 '{filename}' 已存在，将追加数据。")
            existing_df = pd.read_excel(filename, sheet_name=sheet_name)

            # Before concat, ensure columns are consistent if possible, or handle errors
            # For simplicity, assume new data has compatible or a subset of columns.
            # More robust handling might involve aligning columns.
            combined_df = pd.concat([existing_df, df_to_append], ignore_index=True)

            # Deduplication logic, especially for static data
            if 'zhdh' in combined_df.columns and '静态.xlsx' in os.path.basename(filename).lower():
                print(f"为 '{filename}' 基于 'zhdh' 去重。")
                combined_df.drop_duplicates(subset=['zhdh'], keep='last', inplace=True)

            combined_df.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
            print(f"数据已追加到文件 '{filename}'。")

        except Exception as e:
            print(f"❌ 追加数据到 '{filename}' 失败: {e}")
            print("将尝试覆盖写入作为备选方案。")
            try:
                df_to_append.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
                print(f"数据已覆盖写入文件 '{filename}'。")
            except Exception as e_overwrite:
                print(f"❌ 覆盖写入 '{filename}' 也失败: {e_overwrite}")


# --- Main script logic ---
if len(sys.argv) > 1:
    file_path = sys.argv[1].strip().strip("'\"")  # Clean path from args
    print(f"接收到文件路径参数: {file_path}")
else:
    print("未接收到文件路径参数，将使用默认路径。")
    file_path = 'D:\\睿抗\\test交易.xlsx'  # Default path for testing

if not os.path.isfile(file_path):
    print(f"❌错误：文件 '{file_path}' 不存在或不是一个文件。脚本将退出。")
    sys.exit(1)

print(f"正在读取 Excel 文件: {file_path}")
try:
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    print(f"文件中的工作表: {sheet_names}")
    if not sheet_names:
        print(f"❌错误：Excel 文件 '{file_path}' 中没有工作表。")
        sys.exit(1)

    # Assuming data is in the first sheet if not specified, or 'Sheet1'
    target_sheet = 'Sheet1'  # Default or first sheet
    if target_sheet not in sheet_names and sheet_names:
        target_sheet = sheet_names[0]
        print(f"警告：未找到名为 'Sheet1' 的工作表，将使用第一个工作表 '{target_sheet}'。")

    df = excel_file.parse(target_sheet)
    print(f"成功从工作表 '{target_sheet}' 读取数据，行数: {len(df)}")

except FileNotFoundError:
    print(f"❌错误：文件 '{file_path}' 未找到。")
    sys.exit(1)
except Exception as e:
    print(f"❌读取 Excel 文件 '{file_path}' 时发生错误: {e}")
    sys.exit(1)

if df.empty:
    print("读取的DataFrame为空，脚本将退出。")
    sys.exit(0)

# --- Data processing ---
print("\n--- 开始数据处理 ---")
# Standardize column names (case-sensitive)
rename_map = {
    '账户代号': 'zhdh',
    '性别': 'xb',
    '交易流水序号': 'jylsxh',
    '对方账户': 'dfzh',
    '对方行号': 'dfhh',
    '交易日期': 'jyrq',
    '交易时间': 'jysj',
    '交易渠道': 'jyqd',
    '交易金额': 'jyje',
    '对方户名': 'dfhm',  # Make sure this column exists or handle its absence
    '年龄': '年龄',
    '借贷标记': 'jdbj',
    '账户余额': 'zhye',
    '姓名': '姓名'  # Assuming '姓名' is the column for 'dfmccd' calculation
}
actual_rename_map = {k: v for k, v in rename_map.items() if k in df.columns}
df = df.rename(columns=actual_rename_map)
print(f"重命名后的列名: {df.columns.tolist()}")

if '姓名' in df.columns:
    def count_chars(name):
        if pd.isna(name): return 0
        return sum(2 if '\u4e00' <= char <= '\u9fff' else 1 for char in str(name))


    df['dfmccd'] = df['姓名'].apply(count_chars)
    print("已计算 'dfmccd' 列。")
else:
    print("⚠️ '姓名' 列 (用于 dfmccd) 不存在。将创建 'dfmccd' 并填充为0。")
    df['dfmccd'] = 0

if 'jdbj' in df.columns:
    df['jdbj'] = df['jdbj'].map({'是': 1, '否': 0}).fillna(df['jdbj'])
    print("已映射 'jdbj' 列。")
else:
    print("⚠️ 'jdbj' 列不存在。")

if 'xb' in df.columns:
    df['xb'] = df['xb'].map({'男': 1, '女': 0}).fillna(df['xb'])
    print("已映射 'xb' 列。")
else:
    print("⚠️ 'xb' 列不存在，性别信息将缺失。")

# --- Create static_df and transaction_df ---
static_df = None
transaction_df = None  # Initialize

static_columns_renamed = ['zhdh', 'xb', '年龄']
# Check if all necessary columns for static_df exist
if all(col in df.columns for col in static_columns_renamed):
    static_df = df[static_columns_renamed].copy()  # Use .copy()
    static_df = static_df.drop_duplicates(subset='zhdh', keep='first')
    print(f"\n静态数据 DataFrame (static_df) 已生成，行数: {len(static_df)}")
else:
    missing_cols = [col for col in static_columns_renamed if col not in df.columns]
    print(f"⚠️ 静态数据所需列 {missing_cols} 未全部找到，无法生成 static_df。")

# Define columns to drop for transaction_df
cols_to_drop_for_transaction = []
# Add columns from static_df (except 'zhdh') to the drop list if they exist
if 'xb' in static_columns_renamed and 'xb' in df.columns: cols_to_drop_for_transaction.append('xb')
if '年龄' in static_columns_renamed and '年龄' in df.columns: cols_to_drop_for_transaction.append('年龄')
# Also drop the original '姓名' column if it was used for 'dfmccd' and exists
if '姓名' in df.columns and '姓名' in rename_map.values():  # Check if '姓名' was a target in rename_map (i.e., it was kept as '姓名')
    cols_to_drop_for_transaction.append('姓名')

# Ensure all columns to drop actually exist to avoid KeyError
actual_cols_to_drop = [col for col in cols_to_drop_for_transaction if col in df.columns]

if actual_cols_to_drop:
    transaction_df = df.drop(columns=actual_cols_to_drop)
    print(f"\n交易数据 DataFrame (transaction_df) 已生成，行数: {len(transaction_df)}")
else:
    transaction_df = df.copy()  # If nothing to drop, transaction_df is a copy of processed df
    print("⚠️ 没有明确的列从原始数据中移除以生成 transaction_df。")

# --- Save DataFrames ---
output_dir = "data"  # Define output directory relative to script location

if static_df is not None and not static_df.empty:
    static_excel_path = os.path.join(output_dir, "静态.xlsx")
    print(f"\n准备写入/追加到 '{static_excel_path}'...")
    append_df_to_excel(static_excel_path, static_df)
else:
    print("⚠️ 未生成有效的静态数据 DataFrame (static_df)，无法保存文件。")

if transaction_df is not None and not transaction_df.empty:
    transaction_excel_path = os.path.join(output_dir, "交易.xlsx")
    print(f"\n准备写入/追加到 '{transaction_excel_path}'...")
    append_df_to_excel(transaction_excel_path, transaction_df)
else:
    print("⚠️ 未生成有效的交易数据 DataFrame (transaction_df)，无法保存文件。")

print("\n--- 最终完整处理后的 DataFrame (df) 的CSV表示 (用于调试) ---")
print(df.to_csv(sep='\t', na_rep='nan', index=False))  # Print the fully processed df

print("\n脚本执行完毕。")