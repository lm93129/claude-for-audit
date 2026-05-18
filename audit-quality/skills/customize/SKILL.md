---
name: customize
description: >
  局部调整审计质量 Practice Profile——修改质控模式、项目分级、独立性规则、复核层级或缺陷分类，
  无需重跑完整冷启动采访。适用于制度修订、质量管理模式变化或监管要求更新。
argument-hint: "[要修改的章节或内容描述]"
---

# /customize

读取 `~/.claude/plugins/config/claude-for-audit/audit-quality/CLAUDE.md`。

如不存在或仍包含 [PLACEHOLDER] → 提示先跑 `/audit-quality:cold-start-interview`。

## 可调整项

- 质量管理模式
- 质量负责人、独立性负责人、升级联系人
- 项目分级标准与高风险项目触发条件
- 复核层级及适用范围
- 缺陷分类与处理要求
- 独立性关注点
- 职业道德关注点
- 输出路径与命名规则
- 核心制度清单及更新时间
- 连接器状态

## 修改方式

1. 展示当前值
2. 询问用户新值
3. 说明影响（例如：哪些项目会被纳入 EQCR、哪些问题会自动升级）
4. 写回 Practice Profile

## 共享信息提醒

如果用户想改的是事务所/公司级共享信息，应提示同步修改：
`~/.claude/plugins/config/claude-for-audit/company-profile.md`
