#!/usr/bin/env python3
"""
创建Railway部署专用ZIP包
"""

import zipfile
import os

def create_railway_zip():
    """创建Railway部署包"""
    print("📦 创建Railway部署ZIP包")
    print("当前目录:", os.getcwd())
    
    # 列出当前目录文件
    files = os.listdir('.')
    print("📁 目录内容:")
    for f in files:
        print(f"  - {f}")
    
    # 创建ZIP文件
    zip_filename = 'project_for_railway.zip'
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk('.'):
            # 排除系统文件
            exclude_dirs = {'.git', '__pycache__'}
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                # 排除ZIP文件自身和其他系统文件
                if file != zip_filename and not file.startswith('.'):
                    filepath = os.path.join(root, file)
                    # 使用相对路径
                    arcname = os.path.relpath(filepath, '.')
                    zipf.write(filepath, arcname)
                    print(f"✅ 添加: {arcname}")
    
    print(f"\n🎉 Railway部署包创建完成: {zip_filename}")
    print(f"📁 文件大小: {os.path.getsize(zip_filename)} bytes")
    
    # 显示ZIP内容预览
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        files_in_zip = zipf.namelist()
        print(f"📄 ZIP包含 {len(files_in_zip)} 个文件")
        for f in files_in_zip[:15]:  # 显示前15个文件
            print(f"  - {f}")
        if len(files_in_zip) > 15:
            print(f"  - ... 还有 {len(files_in_zip)-15} 个文件")
    
    return zip_filename

def main():
    print("🚀 Railway直接部署方案")
    print("=" * 40)
    
    zip_file = create_railway_zip()
    
    print(f"\n🎯 下一步:")
    print(f"1. 登录Railway: https://railway.app")
    print(f"2. 点击'New Project'")
    print(f"3. 选择'Deploy from GitHub' → 点击'...' → 'Upload .zip'")
    print(f"4. 上传 {zip_file}")
    print(f"5. 等待自动部署")

if __name__ == "__main__":
    main()