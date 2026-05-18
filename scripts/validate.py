#!/usr/bin/env python3
"""
validate.py — 预提交检查脚本

检查项：
1. marketplace.json → 所有 source 路径有效
2. 每个插件 → plugin.json 格式正确
3. 每个插件 → CLAUDE.md 存在（作为 Practice Profile 模板）
4. 每个插件 → 包含 cold-start-interview 技能
5. 所有 JSON 文件语法正确
"""

import json
import glob
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

errors = []

def error(msg):
    errors.append(msg)
    print(f"❌ {msg}")

def ok(msg):
    print(f"  ✓ {msg}")

# 1. 加载 marketplace
marketplace_path = os.path.join(REPO_ROOT, '.claude-plugin', 'marketplace.json')
if not os.path.exists(marketplace_path):
    error("marketplace.json 不存在")
    sys.exit(1)

with open(marketplace_path) as f:
    marketplace = json.load(f)

ok(f"marketplace.json 已加载，含 {len(marketplace.get('plugins', []))} 个插件")

# 2. 验证每个插件
for plugin in marketplace.get('plugins', []):
    name = plugin.get('name')
    source = plugin.get('source')
    
    if not source or source.startswith('http'):
        continue  # 外部插件跳过
    
    plugin_path = os.path.join(REPO_ROOT, source)
    
    if not os.path.exists(plugin_path):
        error(f"{name}: source 路径不存在 {source}")
        continue
    
    # plugin.json
    pj_path = os.path.join(plugin_path, '.claude-plugin', 'plugin.json')
    if not os.path.exists(pj_path):
        error(f"{name}: .claude-plugin/plugin.json 不存在")
    else:
        with open(pj_path) as f:
            pj = json.load(f)
        if not pj.get('name'):
            error(f"{name}: plugin.json 缺少 name")
        if not pj.get('description'):
            error(f"{name}: plugin.json 缺少 description")
    
    # CLAUDE.md (Practice Profile 模板)
    cm_path = os.path.join(plugin_path, 'CLAUDE.md')
    if not os.path.exists(cm_path):
        error(f"{name}: CLAUDE.md (Practice Profile 模板) 不存在")
    
    # cold-start-interview 技能
    csi_path = os.path.join(plugin_path, 'skills', 'cold-start-interview', 'SKILL.md')
    if not os.path.exists(csi_path):
        error(f"{name}: 缺少 cold-start-interview 技能")
    
    # 检查所有 JSON 文件语法
    for jf in glob.glob(os.path.join(plugin_path, '**', '*.json'), recursive=True):
        try:
            with open(jf) as f:
                json.load(f)
        except json.JSONDecodeError as e:
            error(f"{name}: JSON 语法错误 {os.path.relpath(jf)}: {e}")

if errors:
    print(f"\n❌ 发现 {len(errors)} 个错误")
    sys.exit(1)
else:
    print("\n✅ 全部检查通过")
