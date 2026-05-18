#!/usr/bin/env python3
"""
validate.py — 预提交检查脚本

检查项：
1. marketplace.json 存在且 JSON 有效
2. marketplace 中的每个本地插件 source 路径有效
3. 每个插件必须包含：
   - .claude-plugin/plugin.json
   - CLAUDE.md
   - README.md
   - .mcp.json
   - skills/cold-start-interview/SKILL.md
4. plugin.json 与 marketplace.json 中的 name/description 保持一致
5. 每个插件至少有 1 个技能
6. 所有 JSON 文件语法正确
7. 给出 warning：缺少 customize 技能或缺少 agents 目录
"""

import glob
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []


def error(msg):
    errors.append(msg)
    print(f"❌ {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"⚠️  {msg}")


def ok(msg):
    print(f"  ✓ {msg}")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# 1. marketplace
marketplace_path = os.path.join(REPO_ROOT, ".claude-plugin", "marketplace.json")
if not os.path.exists(marketplace_path):
    error("marketplace.json 不存在")
    sys.exit(1)

try:
    marketplace = load_json(marketplace_path)
except Exception as e:
    error(f"marketplace.json 读取失败: {e}")
    sys.exit(1)

plugins = marketplace.get("plugins", [])
ok(f"marketplace.json 已加载，含 {len(plugins)} 个插件")

# 2. validate plugins
for plugin in plugins:
    name = plugin.get("name")
    source = plugin.get("source")
    mp_desc = plugin.get("description")

    if not source:
        error(f"{name}: marketplace.json 中缺少 source")
        continue

    if source.startswith("http"):
        warn(f"{name}: 外部 URL source 未做本地校验")
        continue

    plugin_path = os.path.join(REPO_ROOT, source)
    if not os.path.isdir(plugin_path):
        error(f"{name}: source 路径不存在 {source}")
        continue

    ok(f"{name}: source 路径存在")

    # required files
    required_files = {
        ".claude-plugin/plugin.json": "插件清单",
        "CLAUDE.md": "Practice Profile 模板",
        "README.md": "插件说明",
        ".mcp.json": "MCP 配置",
        "skills/cold-start-interview/SKILL.md": "cold-start-interview 技能",
    }

    for rel, label in required_files.items():
        full = os.path.join(plugin_path, rel)
        if not os.path.exists(full):
            error(f"{name}: 缺少 {label} ({rel})")

    # plugin.json
    pj_path = os.path.join(plugin_path, ".claude-plugin", "plugin.json")
    if os.path.exists(pj_path):
        try:
            pj = load_json(pj_path)
        except Exception as e:
            error(f"{name}: plugin.json 读取失败: {e}")
            pj = None

        if pj:
            pj_name = pj.get("name")
            pj_desc = pj.get("description")
            if not pj_name:
                error(f"{name}: plugin.json 缺少 name")
            if not pj_desc:
                error(f"{name}: plugin.json 缺少 description")
            if pj_name and pj_name != name:
                error(f"{name}: marketplace name 与 plugin.json name 不一致 ({name} != {pj_name})")
            if pj_desc and mp_desc and pj_desc != mp_desc:
                warn(f"{name}: marketplace description 与 plugin.json description 不一致")

    # skills
    skill_files = glob.glob(os.path.join(plugin_path, "skills", "*", "SKILL.md"))
    if not skill_files:
        error(f"{name}: 未发现任何技能文件 skills/*/SKILL.md")
    else:
        ok(f"{name}: 发现 {len(skill_files)} 个技能")

    customize_path = os.path.join(plugin_path, "skills", "customize", "SKILL.md")
    if not os.path.exists(customize_path):
        warn(f"{name}: 缺少 customize 技能（非强制）")

    agents_path = os.path.join(plugin_path, "agents")
    if not os.path.exists(agents_path):
        warn(f"{name}: 缺少 agents 目录（非强制）")

    # JSON syntax in plugin tree
    for jf in glob.glob(os.path.join(plugin_path, "**", "*.json"), recursive=True):
        try:
            load_json(jf)
        except Exception as e:
            error(f"{name}: JSON 语法错误 {os.path.relpath(jf, REPO_ROOT)}: {e}")

# top-level JSON syntax
for jf in glob.glob(os.path.join(REPO_ROOT, "**", "*.json"), recursive=True):
    if "/.git/" in jf:
        continue
    try:
        load_json(jf)
    except Exception as e:
        error(f"JSON 语法错误 {os.path.relpath(jf, REPO_ROOT)}: {e}")

print()
if warnings:
    print(f"⚠️  警告 {len(warnings)} 个")
if errors:
    print(f"❌ 发现 {len(errors)} 个错误")
    sys.exit(1)
else:
    print("✅ 全部检查通过")
    sys.exit(0)
