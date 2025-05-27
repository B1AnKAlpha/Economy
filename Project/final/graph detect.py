import subprocess
from PIL import Image, ImageEnhance, ImageFilter
import os
import tempfile

tesseract_cmd = r".\tesseract.exe"
tessdata_dir = r".\tessdata"

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

    languages = ['eng']
    #'chi_sim',
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
    exit(1)

image_path = r"processed.jpg"

if not os.path.exists(image_path):
    print(f"错误：文件不存在 - {image_path}")
    exit(1)

try:
    with Image.open(image_path) as img:
        print(f"图片已加载 (格式: {img.format}, 尺寸: {img.size})")

        img = img.resize((img.width * 5, img.height * 5), Image.LANCZOS)
        img = img.convert('L')

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(4.0)

        threshold = 127
        img = img.point(lambda p: 255 if p > threshold else 0)

        img.save("processed.jpg")
        print("预处理后的图片已保存为 processed.jpg")

        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
            temp_output_path = temp_file.name[:-4]

        psm_modes = [6, 7, 11]

        for psm in psm_modes:
            print(f"\n尝试OCR配置: --psm {psm}")

            command = [
                tesseract_cmd,
                "processed.jpg",
                temp_output_path,
                "--tessdata-dir", tessdata_dir,
                "-l", "chi_sim+eng",
                "--psm", str(psm)
            ]

            print(f"执行命令: {' '.join(command)}")

            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    check=True
                )

                with open(temp_output_path + '.txt', 'rb') as f:
                    byte_data = f.read()

                print(f"成功获取结果，长度: {len(byte_data)} 字节")

                encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1', 'cp936', 'big5', 'utf-16']

                for encoding in encodings:
                    print(f"  尝试解码: {encoding}")

                    try:
                        text = byte_data.decode(encoding, errors='replace')

                        if text.strip():
                            print(f"识别结果 (PSM {psm}, {encoding}):")
                            print(text)

                            with open(f"ocr_result_psm{psm}_{encoding}.txt", "w", encoding="utf-8") as f:
                                f.write(text)
                            print(f"识别结果已保存到 ocr_result_psm{psm}_{encoding}.txt")

                            break
                        else:
                            print(f"  解码后内容为空 ({encoding})")

                    except Exception as e:
                        print(f"  解码错误 ({encoding}): {e}")

            except subprocess.CalledProcessError as e:
                print(f"命令执行错误: {e.stderr}")
            except Exception as e:
                print(f"发生错误: {e}")



            finally:
                for ext in ['.txt', '.box', '.osd']:
                    file_path = temp_output_path + ext
                    if os.path.exists(file_path):
                        os.remove(file_path)

except Exception as e:
    print(f"发生未知错误: {str(e)}")


from openai import OpenAI
import json

client = OpenAI(
    api_key="sk-hjnjzmakltioklkrozuwzxuonfxavfykshcfhiyawwiyqmln",
    base_url="https://api.siliconflow.cn/v1"
)

input_text = text

prompt = f"""
请总结以下文本，并以JSON格式返回结果，包含以下字段：
- summary: 文本总结（中文，控制在200字以内）
- data: 提取的关键数据（数值、百分比、时间等，需保留单位）

原文：
{input_text}
"""

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "system", "content": "你是专业的数据提取工具，必须返回严格的JSON格式"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.1,
    max_tokens=512
)

result_text = response.choices[0].message.content.strip()
try:
    structured_result = json.loads(result_text)
    print("=" * 50)
    print("JSON格式结果：")
    print("=" * 50)
    print(json.dumps(structured_result, ensure_ascii=False, indent=2))
    print("\n" + "=" * 50)
    print("关键数据：")
    for key, value in structured_result["data"].items():
        print(f"- {key}: {value}")

except json.JSONDecodeError:
    print(result_text)