# 法定审计插件（statutory-audit）

覆盖完整的财务报表审计流程——从风险评估到审计报告签发。

## 安装

```bash
claude plugin install statutory-audit@claude-for-audit
```

## 首次使用

```bash
/statutory-audit:cold-start-interview
```

## 技能命令速查

| 命令 | 对应审计程序 | 何时使用 |
|------|------------|---------|
| `/statutory-audit:cold-start-interview` | 冷启动采访 | 初次安装 |
| `/statutory-audit:risk-assessment` | 风险评估（CSA 1211） | 了解被审计单位 |
| `/statutory-audit:materiality` | 重要性水平（CSA 1221） | 计划阶段 |
| `/statutory-audit:ic-review` | 内部控制评价（CSA 1231） | 了解内控 |
| `/statutory-audit:substantive-testing` | 实质性程序 | 期末审计 |
| `/statutory-audit:sampling` | 审计抽样（CSA 1310） | 抽样测试 |
| `/statutory-audit:confirmations` | 函证（CSA 1312） | 收发函 |
| `/statutory-audit:journal-entry-testing` | 日记账测试 | 舞弊识别 |
| `/statutory-audit:wp-generator` | 底稿生成（CSA 1201） | 编制底稿 |
| `/statutory-audit:analytical-review` | 分析性复核（CSA 1313） | 最终复核 |
| `/statutory-audit:review-notes` | 复核意见 | 三级复核 |
| `/statutory-audit:report-drafting` | 审计报告 | 报告阶段 |

## 审计流程全景

```
┌─ 计划阶段 ─┐
│ 风险评估         │  ← 了解被审计单位、控制环境
│ 重要性水平        │  ← 设定审计阈值
│ 制定审计策略      │
└──────┬──────────┘
       ▼
┌─ 执行阶段 ─┐
│ 控制测试         │  ← ic-review（如计划依赖内控）
│ 实质性程序        │  ← substantive-testing
│ ├ 细节测试        │
│ ├ 函证程序        │  ← confirmations
│ ├ 抽样测试        │  ← sampling
│ └ 异常日记账测试    │  ← journal-entry-testing
│ 分析性复核        │  ← analytical-review（中间阶段）
└──────┬──────────┘
       ▼
┌─ 完成阶段 ─┐
│ 最终分析性复核     │
│ 评价审计发现       │
│ 三级复核           │  ← review-notes
│ 起草审计报告       │  ← report-drafting
└──────────────────┘
```

## 工作底稿体系

本插件生成的底稿遵循中国注协审计工作底稿指引：

```
A/                  # 综合类底稿
├── A1-01-01        审计计划
├── A1-01-02        风险评估
├── A1-01-03        重要性水平
├── A1-99           审计报告
B/                  # 业务循环类
├── B1              销售与收款
├── B2              采购与付款
├── B3              生产与仓储
├── B4              人力资源与薪酬
└── B5              投资与筹资
C/                  # 其他类
├── C1              关联方
├── C2              期后事项
└── C3              持续经营
```

## 依赖

- 需要先完成 cold-start-interview 写入 Practice Profile
- 建议连接企业 ERP MCP 以自动获取会计数据
- 建议连接企查查/天眼查 MCP 以自动获取工商信息