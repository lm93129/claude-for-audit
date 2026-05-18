---
name: cold-start-interview
description: >
  执行司法会计/舞弊审计冷启动采访，学习调查团队的办案方法和关注重点并写入 Practice Profile。
  在插件首次使用、配置文件缺失或仍包含 [PLACEHOLDER] 标记时使用。
argument-hint: "[--redo 重跑] [--check-integrations 仅检查连接器]"
---

# /cold-start-interview

## 检查当前状态

读取 `~/.claude/plugins/config/claude-for-audit/forensic-audit/CLAUDE.md`：
- **不存在** → 开始采访。
- **含 [PLACEHOLDER]** → 询问重头还是继续。
- **已完整且未传 --redo** → 告知已配置。

## Part 1：团队信息

1. 你主要从事哪类司法会计/舞弊审计案件？
   - *（经济犯罪/职务侵占/财务舞弊/商业贿赂/知识产权）*
2. 团队有哪些专业背景的人？*（CPA/CFE/IT 取证/律师）*
3. 年均办案量大约多少？
4. 客户类型以什么为主？
5. 使用哪些数据分析工具？*（IDEA/ACL/Python/SQL/Gephi）*

## Part 2：调查方法论

1. 调查的证明标准是什么？
2. 常用哪些证据获取手段？
3. 是否有电子取证能力，用什么工具？
4. 舞弊风险识别的重点领域是什么？

## Part 3：举报机制

1. 是否有举报渠道？什么形式？
2. 匿名举报如何处理？
3. 举报信息保密的承诺？

## Part 4：文件

要求提供种子材料（越多越好）：
- 过往调查报告 2-3 份（脱敏）
- 常用分析模型或模板
- 证据清单模板
- 适用的法规清单

## 写出 Practice Profile

按模板结构写入目标路径。