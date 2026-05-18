---
name: customize
description: >
  局部调整合规审计 Practice Profile——修改监管重点、风险分级、制度清单、报告风格或整改要求，
  无需重跑完整冷启动采访。适用于组织调整、监管重点变化、制度更新或报告口径变更。
argument-hint: "[要修改的章节或内容描述]"
---

# /customize

读取 `~/.claude/plugins/config/claude-for-audit/compliance-audit/CLAUDE.md`。

如不存在或仍包含 [PLACEHOLDER] → 提示先跑 `/compliance-audit:cold-start-interview`。

## 可调整项

- 合规职能定位与汇报线
- 团队规模与审批人
- 重点监管领域
- 风险评级标准（高/中/低）
- 发现分级标准（重大违规/重要缺陷/一般问题/观察点）
- 适用法规范围
- 证据标准
- 报告输出路径与命名规则
- 重点制度清单及更新时间
- 连接器状态

## 修改方式

1. 展示当前值
2. 询问用户新值
3. 说明下游影响（例如：报告分级会如何变化）
4. 写回 Practice Profile

## 共享信息提醒

如果用户想改的是事务所/公司级共享信息，应提示同步修改：
`~/.claude/plugins/config/claude-for-audit/company-profile.md`
