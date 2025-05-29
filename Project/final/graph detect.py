import csv

import cv2
import pandas as pd
import sys
import base64
import requests
import subprocess
from PIL import Image, ImageEnhance
import os
import tempfile
from openai import OpenAI
import json

from paddleocr import PaddleOCR

tesseract_cmd = r"tesseract.exe"
tessdata_dir = r"./final/tessdata"
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

def check_dependencies():
    try:
        result = subprocess.run(
            [tesseract_cmd, "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"错误：无法运行Tesseract - {result.stderr}")
            return False
        print(f"Tesseract可用，版本: {result.stdout.strip()}")
    except Exception as e:
        print(f"错误：无法运行Tesseract - {e}")
        return False

    languages = ['chi_sim', 'eng']
    #languages = ['eng']
    missing = []
    for lang in languages:
        file_path = os.path.join(tessdata_dir, f'{lang}.traineddata')
        if not os.path.exists(file_path):
            missing.append(lang)
    if missing:
        print(f"警告：缺少语言数据文件: {', '.join(missing)}")
        print(f"请确保 {tessdata_dir} 目录中包含这些文件")
        return False
    print("语言数据文件已找到")
    return True


if not check_dependencies():
    pass

if len(sys.argv) > 1:
    image_path = sys.argv[1].strip().strip("'\"")  # Clean path from args
    print(f"接收到文件路径参数: {image_path}")
else:
    print("未接收到文件路径参数，将使用默认路径。")
    image_path = "./processed1.jpg"
#image_path = r"detect pic.jpg"
#if not os.path.exists(image_path):
#    print(f"错误：文件不存在 - {image_path}")

try:
    with Image.open(image_path) as img:
        print(f"图片已加载 (格式: {img.format}, 尺寸: {img.size})")
        # img = img.resize((img.width * 5, img.height * 5), Image.LANCZOS)
        # img = img.convert('L')
        # enhancer = ImageEnhance.Contrast(img)
        # img = enhancer.enhance(4.0)
        # threshold = 127
        # img = img.point(lambda p: 255 if p > threshold else 0)
        # img.save("./final/processed1.jpg")

        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 使用自适应阈值（适合光照不均）
        thresh = cv2.adaptiveThreshold(gray, 255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY,
                                       11, 2)

        # 可选：反色（Tesseract对黑字白底最敏感）
        thresh = 255 - thresh

        cv2.imwrite("./final/processed1.jpg", thresh)

        # with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
        #     temp_output_path = temp_file.name[:-4]

        from paddleocr import PaddleOCR

        # 初始化 OCR 模型
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")

        # 图像路径
        if len(sys.argv) > 1:
            img_path = "./final/processed1.jpg"
            print(f"接收到文件路径参数: {image_path}")
        else:
            print("未接收到文件路径参数，将使用默认路径。")
            img_path = "./processed1.jpg"

        # OCR 推理
        results = ocr.ocr(img_path)
        text = results[0]["rec_texts"]

        text = ''.join(text)
        print(text)
        #psm_modes = [6, 7, 11]
        # psm_modes = [1]  # 添加更多的PSM模式以测试不同的配置
        # for psm in psm_modes:
        #     config = '--oem 1 --psm 6 -c preserve_interword_spaces=1'
        #     print(f"使用OCR配置: {config}")
        #     command = [
        #                   tesseract_cmd,
        #                   "./final/processed1.jpg",
        #                   temp_output_path,
        #                   "--tessdata-dir", tessdata_dir,
        #                   "-l", "chi_sim+eng"
        #               ] + config.split()
        #     print(f"执行命令: {' '.join(command)}")
        #     try:
        #         result = subprocess.run(
        #             command,
        #             capture_output=True,
        #             text=True,
        #             check=True
        #         )
        #
        #         with open(temp_output_path + '.txt', 'rb') as f:
        #             byte_data = f.read()
        #
        #         print(f"成功获取结果，长度: {len(byte_data)} 字节")
        #
        #         encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1', 'cp936', 'big5', 'utf-16']
        #
        #         for encoding in encodings:
        #             print(f"  尝试解码: {encoding}")
        #
        #             try:
        #                 text = byte_data.decode(encoding, errors='replace')
        #
        #                 if text.strip():
        #                     print(f"识别结果 (PSM {psm}, {encoding}):")
        #                     print(text)
        #
        #                     with open(f"ocr_result_psm{psm}_{encoding}.txt", "w", encoding="utf-8") as f:
        #                         f.write(text)
        #                     print(f"识别结果已保存到 ocr_result_psm{psm}_{encoding}.txt")
        #
        #                     break
        #                 else:
        #                     print(f"  解码后内容为空 ({encoding})")
        #
        #             except Exception as e:
        #                 print(f"  解码错误 ({encoding}): {e}")
        #
        #     except subprocess.CalledProcessError as e:
        #         print(f"命令执行错误: {e.stderr}")
        #     except Exception as e:
        #         print(f"发生错误: {e}")
        #
        #
        #
        #     finally:
        #         for ext in ['.txt', '.box', '.osd']:
        #             file_path = temp_output_path + ext
        #             if os.path.exists(file_path):
        #                 os.remove(file_path)

except Exception as e:
    print(f"发生未知错误: {str(e)}")

client = OpenAI(
    api_key="sk-hjnjzmakltioklkrozuwzxuonfxavfykshcfhiyawwiyqmln",
    base_url="https://api.siliconflow.cn/v1"
)
input_text = text
prompt = f"""
{{input_text}}
"""
a = text+"返回JSON格式，其中字段名为：账户代号，性别，交易流水序号，对方账户，对方行号，交易日期，交易时间，交易渠道，交易金额，姓名，年龄，借贷标记，账户余额。值为对应值，且只能从提示词中获取。借贷标记输出是或否。"
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "system", "content": a},
        {"role": "user", "content": prompt}
    ],
    temperature=0.1,
    max_tokens=512
)
result_text = response.choices[0].message.content.strip()
print("_______")
print(repr(result_text))
print("_______")
s = result_text
if s.startswith('```') and s.endswith('```'):
    s = s.strip('```json\n').rstrip('```')

# 还可以做更稳健的处理：
s = s.replace('```json', '').replace('```', '').strip()
result_text = json.loads(s)
print("_______")
print(result_text)
print("_______")
csv_file = 'output.csv'

# 写入CSV
with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=result_text.keys())
    writer.writeheader()  # 写入表头
    writer.writerow(result_text)  # 写入数据行

print(f'已保存为 {csv_file}')

if len(sys.argv) > 1:
    file_path = './final/output.csv'
else:
    file_path = 'output.csv'

excel_file = pd.read_csv(file_path)



df = excel_file.rename(columns={
    '账户代号': 'zhdh',
    '性别': 'xb',
    '交易流水序号': 'jylsxh',
    '对方账户': 'dfzh',
    '对方行号': 'dfhh',
    '交易日期': 'jyrq',
    '交易时间': 'jysj',
    '交易渠道': 'jyqd',
    '交易金额': 'jyje',
    '姓名': 'dfhm',
    '年龄': '年龄',
    '借贷标记': 'jdbj',
    '账户余额': 'zhye'})


def count_chars(name):
    return sum(2 if '\u4e00' <= char <= '\u9fff' else 1 for char in name)


df['dfmccd'] = df['dfhm'].apply(count_chars)

df['jdbj'] = df['jdbj'].map({'是': 1, '否': 0})

if 'xb' in df.columns:
    df['xb'] = df['xb'].map({'男': 1, '女': 0})
else:
    print("数据中不存在 'xb' 列，请检查输入数据或列名映射。")

static_columns = ['zhdh', 'xb', '年龄']
if all(col in df.columns for col in static_columns):
    static_df = df[static_columns]

    static_df = static_df.drop_duplicates(subset='zhdh', keep='first')
else:
    print("静态数据列未全部找到，请检查列名。")

cols_to_drop = [col for col in static_columns if col != 'zhdh'] + ['dfhm']
if all(col in df.columns for col in cols_to_drop):
    transaction_df = df.drop(cols_to_drop, axis=1)
else:
    print("待删除的列未全部找到，请检查列名。")

if 'static_df' in locals():
    append_df_to_excel('./final/data/静态.xlsx', static_df)
   # static_df.to_excel('./data/静态.xlsx', index=False)
else:
    print("未生成静态数据 DataFrame，无法保存文件。")

if 'transaction_df' in locals():
    append_df_to_excel('./final/data/交易.xlsx', transaction_df)
    #transaction_df.to_excel('./data/交易.xlsx', index=False)
else:
    print("未生成交易数据 DataFrame，无法保存文件。")

print(df.to_csv(sep='\t', na_rep='nan'))
