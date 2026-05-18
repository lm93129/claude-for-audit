---
name: customize
description: >
  局部调整司法会计 Practice Profile ——改一个参数不重跑采访。
  当用户说"改我的调查方法"、"更新案件类型"时使用。
argument-hint: "[要修改的章节或内容描述]"
---

# /customize

读取 `~/.claude/plugins/config/claude-for-audit/forensic-audit/CLAUDE.md`。

如不存在或含 [PLACEHOLDER] → 提示先跑 cold-start-interview。

**可调整项：**

- **办案类型** —— 经济犯罪/职务侵占/财务舞弊
- **舞弊三角权重** —— 压力/机会/合理化的关注比重
- **证明标准** —— 优势证据/清晰且有说服力/排除合理怀疑
- **分析工具** —— IDEA/ACL/Python/SQL 是否可用
- **举报渠道** —— 热线/邮箱/平台信息
- **监管机构对接** —— 纪委监委/公安/证监会的报送要求
- **常用法规引用** —— 办案依据的法条清单