# -*- mode: python ; coding: utf-8 -*-

import os
import glob
from PyInstaller.utils.hooks import collect_submodules

project_dir = os.path.abspath('.')

# 自动收集模块
hidden_imports = collect_submodules("modules") + collect_submodules("widgets") + collect_submodules("pymysql")

# 辅助函数：收集指定文件夹中所有特定类型的文件
def collect_files(pattern, target_folder):
    files = glob.glob(pattern, recursive=True)
    return [(f, os.path.join(target_folder, os.path.relpath(f, start=project_dir))) for f in files]

# 基础数据文件
datas = [
    ('icon.ico', '.'),
    ('main.ui', '.'),
    ('modules/resources_rc.py', 'modules'),
]

# 添加 qss 和图片资源
datas += collect_files(os.path.join(project_dir, 'themes', '*.qss'), 'themes')
datas += collect_files(os.path.join(project_dir, 'images', 'icons', '*.png'), 'images/icons')
datas += collect_files(os.path.join(project_dir, 'images', 'images', '*.png'), 'images/images')

# ✅ 添加 widgets 目录下所有图片资源（png/jpg/jpeg/ico）
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.ico']
for ext in image_extensions:
    datas += collect_files(os.path.join(project_dir, 'widgets', '**', ext), 'widgets')

# 编译打包配置
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[project_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FraudShield',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='icon.ico',
)

coll = COLLECT(
    exe,admin
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FraudShield',
)
