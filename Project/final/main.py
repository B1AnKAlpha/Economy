import os
import sys
import subprocess
import re # Still used by parse_file_list_input if main() is called directly

# --- Constants for output files ---
OUTPUT_DIR = "data"
STATIC_FILE_NAME = "静态.xlsx"
TRANSACTION_FILE_NAME = "交易.xlsx"

STATIC_FILE_PATH = os.path.join(OUTPUT_DIR, STATIC_FILE_NAME)
TRANSACTION_FILE_PATH = os.path.join(OUTPUT_DIR, TRANSACTION_FILE_NAME)


def detect_input_type(file_path):
    if not isinstance(file_path, str):
        return 'invalid_path_type'
    cleaned_path = file_path.strip().strip("'\"") # Clean path once at detection
    if not os.path.isfile(cleaned_path):
        return 'not_a_file'
    ext = os.path.splitext(cleaned_path)[-1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.bmp']:
        return 'image'
    elif ext in ['.csv', '.xlsx']:
        return 'csv'
    elif ext == '.txt':
        return 'textfile'
    else:
        return 'unknown_file_type'

def run_script(script_name, *args):
    # Ensure args are strings, especially file paths
    str_args = [str(arg) for arg in args]
    cmd = [sys.executable, script_name] + str_args
    print(f"运行命令: {' '.join(cmd)}")
    try:
        process = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding='utf-8')
        if process.stdout:
            print(f"--- STDOUT from {script_name} ---")
            print(process.stdout)
        if process.stderr:
            print(f"--- STDERR from {script_name} ---")
            print(process.stderr)
        print(f"--- {script_name} 完成 ---")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 执行 '{script_name}' 失败 (参数: {str_args}). 返回码: {e.returncode}", file=sys.stderr)
        if e.stdout: print(f"--- STDOUT on error ---\n{e.stdout}", file=sys.stderr)
        if e.stderr: print(f"--- STDERR on error ---\n{e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print(f"❌ 错误: 脚本 '{script_name}' 或 Python 解释器 '{sys.executable}' 未找到。", file=sys.stderr)
        return False

def delete_file_if_exists(file_path):
    """Safely deletes a file if it exists."""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"已删除旧文件: {file_path}")
    except OSError as e:
        print(f"❌ 删除文件 {file_path} 失败: {e}", file=sys.stderr)

# --- Core processing function ---
def process_input_files(list_of_file_paths):
    """
    Processes a list of file paths:
    1. Cleans old static/transaction files.
    2. Iterates through each file path, detects type, and runs the corresponding script.
    3. Runs pre6.py if any file was processed.
    """
    if not isinstance(list_of_file_paths, list):
        print("❌ 错误: process_input_files 需要一个文件路径列表作为参数。")
        return

    print("\n--- 清理旧的输出文件 ---")
    if not os.path.exists(OUTPUT_DIR):
        print(f"输出目录 '{OUTPUT_DIR}' 不存在，无需清理文件。")
    else:
        delete_file_if_exists(STATIC_FILE_PATH)
        delete_file_if_exists(TRANSACTION_FILE_PATH)
    print("--- 清理完成 ---\n")

    if not list_of_file_paths:
        print("提供的文件路径列表为空，不执行任何处理。")
        return

    print(f"接收到的文件列表进行处理: {list_of_file_paths}")

    processed_any_file = False # Changed variable name for clarity

    for file_path_item in list_of_file_paths:
        # Clean the path item itself, as it comes directly from the list
        # detect_input_type will also clean, but good to be consistent
        current_file_path = str(file_path_item).strip().strip("'\"")
        if not current_file_path: # Skip if path becomes empty after stripping
            continue

        print(f"\n处理文件: {current_file_path}")
        input_type = detect_input_type(current_file_path) # Pass the cleaned path

        script_to_run = None
        if input_type == 'image':
            print(f"检测到图片文件: {current_file_path}")
            script_to_run = './final/Graph detect.py'
        elif input_type == 'csv':
            print(f"检测到CSV/Excel文件: {current_file_path}")
            script_to_run = './final/CSV detect.py'
        elif input_type == 'textfile':
            print(f"检测到文本文件: {current_file_path}")
            script_to_run = './final/Text dect.py'
        elif input_type == 'not_a_file':
            print(f"⚠️ 警告: '{current_file_path}' 不是一个有效的文件或路径不存在，已跳过。")
        elif input_type == 'invalid_path_type':
            print(f"⚠️ 警告: '{current_file_path}' 路径类型无效，已跳过。")
        else:  # 'unknown_file_type'
            print(f"⚠️ 警告: 无法识别文件 '{current_file_path}' 的类型 (类型: {input_type})，已跳过。")

        if script_to_run:
            run_script(script_to_run, current_file_path) # Pass the cleaned path
            processed_any_file = True

    if processed_any_file:
        print("\n所有识别的文件处理完毕（或尝试处理完毕）。")
        print("现在运行 pre6.py...")
        run_script('./final/pre6.py')
    elif list_of_file_paths: # Files were provided but none were processable
        print("\n提供的文件中没有可识别或处理的文件，不运行 pre6.py。")
    # No else needed for empty list_of_file_paths as it's handled earlier

# --- Function for parsing command-line input (kept for direct script execution) ---
def parse_file_list_input_from_string(input_str):
    """ Parses a string (e.g., from command line input) into a list of file paths. """
    input_str = input_str.strip()
    files = []
    if input_str.startswith('[') and input_str.endswith(']'):
        content = input_str[1:-1].strip()
        if not content: return []
        potential_files = re.split(r'\s+', content) # Simple space split for bracketed list
        for pf in potential_files:
            pf_cleaned = pf.strip().strip("'\"")
            if pf_cleaned: files.append(pf_cleaned)
        return files
    if ',' in input_str: # Comma-separated
        potential_files = input_str.split(',')
        for pf in potential_files:
            pf_cleaned = pf.strip().strip("'\"")
            if pf_cleaned: files.append(pf_cleaned)
        return files
    # Single path
    single_path_cleaned = input_str.strip().strip("'\"")
    if single_path_cleaned: return [single_path_cleaned]
    return []

def main_interactive():
    """Handles interactive input when the script is run directly."""
    user_input_str = input(
        "请输入文件路径(单个路径，或用逗号分隔的多个路径，或用方括号包裹的空格分隔列表如 '[file1 file2.csv]'):\n").strip()

    if not user_input_str:
        print("未输入任何文件路径。")
        return

    # Use the string parsing function here
    file_paths_from_input = parse_file_list_input_from_string(user_input_str)

    if not file_paths_from_input:
        print("无法从输入中解析出有效的文件路径。")
        return

    process_input_files(file_paths_from_input)


if __name__ == '__main__':
    # This part is executed when the script is run directly
    main_interactive()