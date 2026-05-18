# 开发计划

## Phase 1：骨架搭建（已完成）

- [x] README.md — 项目总览
- [x] ARCHITECTURE.md — 架构设计
- [x] QUICKSTART.md — 安装指引
- [x] CLAUDE.md — 仓库级开发指南
- [x] .claude-plugin/marketplace.json — 插件注册表
- [x] .gitignore
- [x] statutory-audit 插件骨架 + Practice Profile 模板
- [x] 5 个其他插件 README（internal-audit ~ audit-quality）
- [x] 共享参考资料（firm-profile-template, auditing-standards）
- [x] 验证脚本（validate.py, lint-independence.py）
- [x] managed-agent 模板示例（continuous-audit）
- [x] 外部插件目录

## Phase 2：核心技能开发（statutory-audit）

- [x] skills/cold-start-interview/SKILL.md — 冷启动采访
- [x] skills/customize/SKILL.md — 局部调整
- [x] skills/materiality/SKILL.md — 重要性水平
- [x] skills/analytical-review/SKILL.md — 分析性复核
- [x] skills/confirmations/SKILL.md — 函证程序
- [x] skills/journal-entry-testing/SKILL.md — 异常日记账
- [x] skills/risk-assessment/SKILL.md — 风险评估（CSA 1211）
- [x] skills/ic-review/SKILL.md — 内部控制评价（CSA 1231）
- [x] skills/substantive-testing/SKILL.md — 实质性程序
- [x] skills/sampling/SKILL.md — 审计抽样（CSA 1310）
- [x] skills/wp-generator/SKILL.md — 底稿生成（CSA 1131）
- [x] skills/review-notes/SKILL.md — 三级复核管理
- [x] skills/report-drafting/SKILL.md — 审计报告起草（CSA 1501~1504）
- [x] agents/deadline-watcher.md — 截止日监控代理

## Phase 3：专项插件开发

- [ ] internal-audit — 7 个技能
- [ ] compliance-audit — 5 个技能
- [ ] it-audit — 5 个技能
- [ ] forensic-audit — 5 个技能
- [ ] audit-quality — 5 个技能

## Phase 4：增强功能

- [ ] 底稿模板参考（.xlsx 模板文件）
- [ ] 与企业微信/飞书/钉钉的 MCP 连接器配置指南
- [ ] 与用友/金蝶 ERP 的连接器配置指南
- [ ] 电子函证集成指南
- [ ] 持续审计 cookbook 完整化
- [ ] 截止日监控 cookbook
- [ ] 异常预警 cookbook

## Phase 5：测试与发布

- [ ] 完整 validate.py 通过
- [ ] 安装测试（Cowork + Claude Code）
- [ ] cold-start-interview 全流程测试
- [ ] 至少一个完整审计案例测试
- [ ] LICENSE 添加
- [ ] GitHub 仓库发布