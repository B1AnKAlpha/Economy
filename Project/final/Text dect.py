import os
import sys
from io import StringIO
import pandas as pd

# --- Helper function to append DataFrame to an Excel file ---
def append_df_to_excel(filename, df, sheet_name='Sheet1', index=False, startrow=None, **to_excel_kwargs):
    """
    Append a DataFrame to an existing Excel file or create a new file.

    Args:
        filename (str): Path to the Excel file.
        df (pd.DataFrame): DataFrame to append.
        sheet_name (str): Name of the Excel sheet.
        index (bool): Whether to write DataFrame index.
        startrow (int, optional): If provided, uses openpyxl to append.
                                 Otherwise, reads existing, concats, and overwrites.
        **to_excel_kwargs: Additional arguments to pass to df.to_excel().
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    if not os.path.isfile(filename):
        # File does not exist, create it
        print(f"文件 '{filename}' 不存在，将创建新文件。")
        df.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
        print(f"数据已写入新文件 '{filename}'。")
    else:
        # File exists, append data
        try:
            # Option 1: Using pd.ExcelWriter with mode 'a' (requires openpyxl or xlsxwriter)
            # This method is cleaner if you have the right engine and version.
            # It might need adjustments based on pandas version.
            # For simplicity and broader compatibility, let's use read-concat-write first.

            # Option 2: Read existing, concatenate, then write (more robust across pandas versions for simple append)
            print(f"文件 '{filename}' 已存在，将追加数据。")
            existing_df = pd.read_excel(filename, sheet_name=sheet_name)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            # Remove duplicates after appending, especially for static_df based on 'zhdh'
            if 'zhdh' in combined_df.columns and '静态' in filename: # Heuristic for static_df
                 # Keep the last entry for a 'zhdh' if duplicates arise from appending the same data
                 # Or 'first' if you want to keep the originally loaded data
                 combined_df.drop_duplicates(subset=['zhdh'], keep='last', inplace=True)

            combined_df.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
            print(f"数据已追加到文件 '{filename}'。")

        except Exception as e:
            print(f"❌ 追加数据到 '{filename}' 失败: {e}")
            print("将尝试覆盖写入作为备选方案。")
            try:
                df.to_excel(filename, sheet_name=sheet_name, index=index, **to_excel_kwargs)
                print(f"数据已覆盖写入文件 '{filename}'。")
            except Exception as e_overwrite:
                print(f"❌ 覆盖写入 '{filename}' 也失败: {e_overwrite}")

# --- Main script logic ---
if len(sys.argv) > 1:
    input_path = sys.argv[1]
    print(f"接收到命令行参数（文件路径）：{input_path}")
    if os.path.isfile(input_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                input_text = f.read()
            print(f"成功读取文件内容，长度: {len(input_text)}")
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
            sys.exit(1)
    else:
        print("❌ 传入的路径不是文件或不存在")
        sys.exit(1)
else:
    print("未传入参数，使用默认内嵌数据")
    input_text = """交易流水序号\t账户代号\t借贷标记\t交易金额\t账户余额\t对方行号\t交易日期\t交易时间\t交易渠道\t对方账户\t姓名\t年龄\t性别
1\t3242244504235523\t是\t349.75\t356.86\tc01\t2020/3/1\t4:41:09\t网银\t12345\t于沛豪\t23\t男
2\t3242244504235523\t否\t61.61\t295.25\tc02\t2020/3/1\t4:42:38\t转账\t54321\t韩宇海\t32\t女
3\t3242244504235523\t否\t2\t293.25\tc03\t2020/3/1\t12:58:27\t转账\t134521\t于沛豪\t23\t男
4\t3242244504235523\t否\t185\t108.25\tc04\t2020/3/1\t17:06:58\t自助\t66661\tHello World\t111\t女"""

# Initialize df to None or an empty DataFrame to handle potential read errors gracefully
df = None
try:
    df = pd.read_csv(StringIO(input_text.strip()), sep='\t')
    print("成功读取数据，行数:", len(df))
    if not df.empty:
        print("读取的DataFrame头部:")
        print(df.head())
    else:
        print("DataFrame 为空。")
except Exception as e:
    print(f"❌ 读取CSV数据到DataFrame失败: {e}")
    if input_text: # Only print debug info if input_text was populated
        print("--- DEBUG INFO ---")
        print("传递给 StringIO 的文本内容 (首200字符):")
        print(f"\"{input_text.strip()[:200]}...\"")
        print("--- END DEBUG INFO ---")
    sys.exit(1)

if df is None or df.empty:
    print("没有有效数据被读取，脚本将退出。")
    sys.exit(0) # Exit gracefully if no data

print("\n✅ 读取成功！数据行数：", len(df))
print("_____________原始数据 (头部) _____________")
print(df.head())
print("________________________________")

# --- Data processing ---
# Standardize column names (case-sensitive)
# Make sure the keys in rename_map match EXACTLY (case and content) what pd.read_csv produces
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
    # '对方户名': 'dfhm', # Assuming this might not always be present; handle carefully
    '年龄': '年龄',     # Keeping original if it's '年龄'
    '借贷标记': 'jdbj',
    '账户余额': 'zhye',
    '姓名': '姓名'      # Keeping original if it's '姓名' for 'dfmccd' calculation
}
# Only rename columns that actually exist in the DataFrame
actual_rename_map = {k: v for k, v in rename_map.items() if k in df.columns}
df = df.rename(columns=actual_rename_map)
print("\n重命名后的列名:", df.columns.tolist())


# Calculate 'dfmccd' (对方户名长度) - assuming '姓名' column represents this
if '姓名' in df.columns:
    def count_chars(name):
        if pd.isna(name): return 0 # Handle NaN names
        return sum(2 if '\u4e00' <= char <= '\u9fff' else 1 for char in str(name))
    df['dfmccd'] = df['姓名'].apply(count_chars)
    print("已计算 'dfmccd' 列。")
else:
    print("⚠️ '姓名' 列不存在，无法计算 'dfmccd'。")
    df['dfmccd'] = 0 # Create with default if needed downstream

# Map 'jdbj'
if 'jdbj' in df.columns:
    df['jdbj'] = df['jdbj'].map({'是': 1, '否': 0}).fillna(df['jdbj']) # Fillna to keep original if not mapped
    print("已映射 'jdbj' 列。")
else:
    print("⚠️ 'jdbj' 列不存在。")

# Map 'xb'
if 'xb' in df.columns:
    df['xb'] = df['xb'].map({'男': 1, '女': 0}).fillna(df['xb']) # Fillna to keep original if not mapped
    print("已映射 'xb' 列。")
else:
    print("⚠️ 'xb' 列不存在，性别信息将缺失。")

# --- Create static_df and transaction_df ---
static_df = None
transaction_df = None

# Define columns for static_df - ensure these are the RENAMED column names
static_columns_renamed = ['zhdh', 'xb', '年龄'] # '年龄' is already the target name
# Check if all necessary columns for static_df exist after renaming
if all(col in df.columns for col in static_columns_renamed):
    static_df = df[static_columns_renamed].copy() # Use .copy() to avoid SettingWithCopyWarning
    static_df = static_df.drop_duplicates(subset='zhdh', keep='first')
    print(f"\n静态数据 DataFrame (static_df) 已生成，行数: {len(static_df)}")
else:
    missing_cols = [col for col in static_columns_renamed if col not in df.columns]
    print(f"⚠️ 静态数据所需列 {missing_cols} 未全部找到，无法生成 static_df。")

# Define columns to drop for transaction_df
# These should be columns from static_df (except 'zhdh') plus original '姓名' if it was used
cols_to_drop_for_transaction = []
if 'xb' in static_columns_renamed and 'xb' in df.columns : cols_to_drop_for_transaction.append('xb')
if '年龄' in static_columns_renamed and '年龄' in df.columns : cols_to_drop_for_transaction.append('年龄')
if '姓名' in df.columns: cols_to_drop_for_transaction.append('姓名') # Original '姓名' column

# Ensure all columns to drop actually exist to avoid KeyError
actual_cols_to_drop = [col for col in cols_to_drop_for_transaction if col in df.columns]

if actual_cols_to_drop:
    transaction_df = df.drop(columns=actual_cols_to_drop)
    print(f"\n交易数据 DataFrame (transaction_df) 已生成，行数: {len(transaction_df)}")
    # print("Transaction_df columns:", transaction_df.columns.tolist())
else:
    # If nothing to drop (e.g. static columns weren't present), transaction_df is essentially df
    transaction_df = df.copy()
    print("⚠️ 没有明确的列从原始数据中移除以生成 transaction_df，transaction_df 为原始数据的副本。")


# --- Save DataFrames ---
output_dir = "data" # Define output directory

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

print("\n--- 最终合并的 DataFrame (用于CSV输出预览) ---")
# Outputting the processed df to CSV, which might be different from transaction_df if columns were dropped
# For consistency, you might want to save transaction_df to CSV if that's the final "transactional" view
# Or df if you want the most complete view after all processing.
# Current code prints df.to_csv(...) which is the state after renaming and mapping, but before dropping for transaction_df.
# Let's print transaction_df to CSV if it exists and is the primary output for transactions.
if transaction_df is not None:
    print("Transaction_df (将被写入交易.xlsx) 的CSV表示:")
    print(transaction_df.to_csv(sep='\t', na_rep='nan', index=False))
else:
    print("Transaction_df 未有效生成，无法输出其CSV表示。")

print("\n脚本执行完毕。")