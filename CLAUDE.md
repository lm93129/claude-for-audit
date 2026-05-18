# CLAUDE.md

`claude-for-audit` 是一个 Claude Code 插件市场——六个审计领域的一手插件和三个 managed-agent 模板。大部分工作涉及编辑提示词内容（技能、代理、钩子）、插件元数据或 Cookbook 配置——而非应用程序代码。

## 仓库布局

```
<plugin>/                         # 6 个一手插件
  .claude-plugin/plugin.json      # 插件清单
  .mcp.json                       # MCP 服务器配置
  CLAUDE.md                       # 实践档案模板（由 cold-start 写入）
  README.md                       # 插件文档
  skills/<name>/SKILL.md          # 技能定义
  agents/<name>.md                # 定时代理定义
  hooks/hooks.json                # 钩子配置
  .gitignore
managed-agent-cookbooks/<name>/   # CMA agent.yaml + subagents/ + steering-examples.json
scripts/                          # validate.py, lint-independence.py, deploy-managed-agent.sh
references/                       # 共享模板与参考（审计准则、会计准则、法规）
```

## 验证——PR 前必做

```bash
# 1. 市场 + 插件 schema 验证
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done

# 2. 独立性检查
python3 scripts/lint-independence.py

# 3. JSON/YAML 语法检查
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
```

## 约定

- `marketplace.json` 中的 `name`、`description`、`author` 必须与插件的 `plugin.json` 保持一致
- 所有 SKILL.md 必须使用 `description` 字段准确描述触发条件，含二级 `argument-hint` 可选
- 每个插件必须包含 `cold-start-interview` 技能——这是首个必跑技能
- 每个插件的 `CLAUDE.md` 是**模板**，写入的是用户的 Practice Profile，不是项目上下文

## 格式规范

- JSON 和 `.mcp.json` 使用 2 空格缩进
- 每个文本文件末尾换行
- 无尾部空格
- Markdown 表格保持列数一致