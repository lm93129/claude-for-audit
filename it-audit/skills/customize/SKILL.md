---
name: customize
description: >
  局部调整 IT 审计 Practice Profile——修改系统范围、控制重点、缺陷分级、参考框架或报告风格，
  无需重跑完整冷启动采访。适用于系统环境变化、上云/迁移、团队重组或审计重点切换。
argument-hint: "[要修改的章节或内容描述]"
---

# /customize

读取 `~/.claude/plugins/config/claude-for-audit/it-audit/CLAUDE.md`。

如不存在或仍包含 [PLACEHOLDER] → 提示先跑 `/it-audit:cold-start-interview`。

## 可调整项

- IT 审计定位与汇报线
- 团队角色与审批人
- 主要系统类型与部署模式
- 范围偏好（ITGC / 应用控制 / 迁移 / 安全 / CAATT）
- 缺陷分类标准
- 参考框架（COBIT / 等保 2.0 / ISO 27001 / 内部制度）
- 输出路径与命名规则
- 重点制度清单
- 连接器状态（ITSM / IAM / CMDB / SIEM / 文档库）

## 修改方式

1. 展示当前值
2. 询问用户新值
3. 说明下游影响（例如：缺陷定级和测试重点如何变化）
4. 写回 Practice Profile

## 共享信息提醒

如果用户想改的是事务所/公司级共享信息，应提示同步修改：
`~/.claude/plugins/config/claude-for-audit/company-profile.md`
