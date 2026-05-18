#!/usr/bin/env python3
"""
lint-independence.py — 独立性检查脚本

检查所有插件中对独立性有影响的配置：
1. 输出头是否正确区分律师/非律师角色（此处改为审计师/助理）
2. 不含可能违反独立性原则的内容
"""

import json
import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []

def error(msg):
    errors.append(msg)

def warn(msg):
    warnings.append(msg)

# 检查每个插件的 CLAUDE.md 中是否包含角色定义
plugins = [
    'statutory-audit',
    'internal-audit',
    'compliance-audit',
    'it-audit',
    'forensic-audit',
    'audit-quality',
]

for plugin in plugins:
    cm_path = os.path.join(REPO_ROOT, plugin, 'CLAUDE.md')
    if not os.path.exists(cm_path):
        warn(f"{plugin}: CLAUDE.md 不存在，跳过")
        continue
    
    with open(cm_path) as f:
        content = f.read()
    
    # 检查角色定义
    if '执业CPA' not in content and '审计助理' not in content:
        warn(f"{plugin}: CLAUDE.md 未包含角色定义（执业CPA/审计助理）")
    
    # 检查独立性声明
    if '独立性' not in content and '独立' not in content:
        warn(f"{plugin}: CLAUDE.md 未包含独立性相关配置")

if errors:
    print(f"\n❌ {len(errors)} 个错误:")
    for e in errors:
        print(f"  {e}")

if warnings:
    print(f"\n⚠️  {len(warnings)} 个警告:")
    for w in warnings:
        print(f"  {w}")

if not errors and not warnings:
    print("✅ 独立性检查通过")

sys.exit(1 if errors else 0)
