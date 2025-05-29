import subprocess

result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True)
lines = result.stdout.splitlines()

with open('requirements.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        # 过滤掉包含本地路径的包
        if '@ file://' in line:
            # 如果想保留包名，可以做简单截断
            pkg = line.split('@')[0].strip()
            # 也可以跳过，视需求
            # f.write(pkg + '\n')
            continue
        else:
            f.write(line + '\n')

print("清理后的 requirements.txt 生成完毕")
