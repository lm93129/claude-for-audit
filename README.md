# Claude for Audit

面向中国审计与合规场景的 Claude 插件仓库，覆盖财务审计中最常见的工作流——法定审计、内部审计、合规审计、IT 审计、司法会计以及审计质量控制。

> 首次使用？从 `QUICKSTART.md` 开始。
>
> 当前状态：本仓库已完成 6 个核心插件的第一版骨架与技能集，可作为后续产品化、插件化和团队定制化的基础版本。

[!IMPORTANT]
本仓库所有输出均为审计人员的工作底稿草稿，不构成审计结论、鉴证意见、监管结论或替代专业判断。每个技能均设有职业道德护栏：来源标注、角色门控、整改闭环、复核节点和独立性约束。最终判断仍由具备授权的专业人员负责。

## 已实现状态

目前仓库已完成以下内容：

- 6 个核心插件全部建成
- 46 个技能已落地
- 3 个定时/持续监控代理已落地
- 统一的 Practice Profile 机制已建立
- 统一的校验脚本与仓库规范已建立

### 完成度总览

| 插件 | 状态 | 技能数 | 代理数 | 说明 |
|------|------|--------|--------|------|
| `statutory-audit` | 已实现 | 13 | 1 | 法定审计主流程完整 |
| `internal-audit` | 已实现 | 8 | 2 | 内审项目与整改闭环完整 |
| `compliance-audit` | 已实现 | 6 | 0 | 合规审计主线完整 |
| `it-audit` | 已实现 | 6 | 0 | ITGC/应用控制/迁移/安全/CAATT 完整 |
| `forensic-audit` | 已实现 | 7 | 0 | 舞弊调查与电子取证完整 |
| `audit-quality` | 已实现 | 6 | 0 | 质量控制与职业道德约束完整 |

说明：这里的“已实现”是指插件骨架、Practice Profile 和核心技能已落地，可继续进入增强与产品化阶段；不代表已经过真实客户环境集成验证。

## 仓库结构

```
statutory-audit/            # 法定审计——财务报表审计（核心插件）
internal-audit/             # 内部审计——流程审计、经营审计
compliance-audit/           # 合规审计——个保法、反商业贿赂、税务合规
it-audit/                   # IT 审计——一般控制、应用控制、CAATT
forensic-audit/             # 司法会计——舞弊识别、电子取证
audit-quality/              # 审计质量监控——独立性、复核、职业道德
external_plugins/           # 合作伙伴插件（用友/金蝶/企查查等）
managed-agent-cookbooks/    # Managed Agent 模板
  continuous-audit/         # 持续审计
  deadline-monitor/         # 截止日监控（预留）
  anomaly-detector/         # 异常预警（预留）
references/                 # 共享参考资料
scripts/                    # 验证和部署脚本
```

## 设计原则

本仓库的设计融合了两个 Anthropic 官方参考仓库的最佳实践：

| 来源 | 借鉴点 |
|------|--------|
| `financial-services` | 金融领域专业技能、Excel 工作底稿生成、数据连接器（MCP） |
| `claude-for-legal` | Cold-start interview、Practice Profile、职业道德护栏、角色门控、定时 Agent |

### 核心设计理念

1. 一源双路（Two Ways from One Source）
   - 每个插件既可作为 Cowork 插件安装，也可通过 Managed Agent API 部署
2. 冷启动优先
   - 安装后先跑 `cold-start-interview`，采集团队方法论，写入 Practice Profile
3. 零默认原则
   - 关键判断参数来自 Practice Profile，不预设事务所/团队专属结论
4. 证据链完整性
   - 每个结论都应能追溯到来源、方法和记录
5. 发现 ≠ 结论
   - 输出默认是“初步发现，需经复核”
6. 插件分层清晰
   - 审计执行、舞弊调查、质量控制、IT 审计和合规审计各自独立，但可相互协作

## 插件列表（已实现）

### 1. 法定审计 `statutory-audit`

已实现技能：

- `cold-start-interview`
- `customize`
- `risk-assessment`
- `materiality`
- `ic-review`
- `substantive-testing`
- `sampling`
- `confirmations`
- `journal-entry-testing`
- `wp-generator`
- `analytical-review`
- `review-notes`
- `report-drafting`

已实现代理：

- `deadline-watcher`

覆盖能力：
- 从风险评估到报告起草的法定审计完整主链路
- 重要性水平、抽样、函证、底稿、复核、报告全部可落地
- 与中国注册会计师审计准则（CSA）对齐

### 2. 内部审计 `internal-audit`

已实现技能：

- `cold-start-interview`
- `customize`
- `audit-program`
- `process-mapping`
- `risk-control-matrix`
- `data-analytics`
- `finding-drafting`
- `remediation-tracking`
- `report-drafting`

已实现代理：

- `continuous-monitor`
- `finding-follow-up`

覆盖能力：
- 从立项、流程梳理、RCM、发现起草到整改闭环的完整内审流程
- 支持连续监控和整改跟踪
- 偏流程优化和管理改进，而非对外鉴证

### 3. 合规审计 `compliance-audit`

已实现技能：

- `cold-start-interview`
- `regulatory-checker`
- `pip-compliance`
- `anti-corruption`
- `tax-compliance`
- `sox-like`

覆盖能力：
- 中国监管语境下的合规审计主线
- 重点覆盖：个保法、数据安全、反商业贿赂、税务与内控合规评价
- 输出以内部整改和合规治理为主

### 4. IT 审计 `it-audit`

已实现技能：

- `cold-start-interview`
- `gc-attestation`
- `application-control`
- `data-migration-audit`
- `cybersecurity-review`
- `caatt`

覆盖能力：
- 覆盖 ITGC、应用控制、迁移审计、网络安全和 CAATT
- 面向 ERP、OA、CRM、数据平台等系统环境
- 支撑财务依赖系统和关键业务系统的可信性评价

### 5. 司法会计 `forensic-audit`

已实现技能：

- `cold-start-interview`
- `customize`
- `red-flags`
- `benford-analysis`
- `data-forensics`
- `transaction-analysis`
- `whistleblower-triage`

覆盖能力：
- 舞弊红旗识别
- 本福特定律检验
- 异常交易穿透分析
- 电子取证与证据链管理
- 举报线索三色分类与分流

### 6. 审计质量监控 `audit-quality`

已实现技能：

- `cold-start-interview`
- `independence-check`
- `engagement-review`
- `peer-review`
- `documentation-qc`
- `ethics-screener`

覆盖能力：
- 独立性检查
- 项目质量复核
- 同业互查/内部抽查
- 底稿质量控制
- 职业道德风险筛查

这个插件是整个仓库的“质量约束层”。

## 方法论定位

本仓库默认以中国审计与合规语境为主：

- 法定审计：以中国注册会计师审计准则（CSA）为核心
- 合规审计：以中国监管框架为核心（个保法、数据安全法、税收征管法、反不正当竞争法等）
- 内控/IT：参考 COSO、COBIT、等保 2.0、ISO 27001、IPPF 等框架

## 当前仍待增强的方向

虽然 6 大插件已完成第一版，但仓库仍有一些明确的下一阶段工作：

1. 增加更多定时代理
   - 合规巡检代理
   - IT 告警抽查代理
   - 年度质量回顾代理

2. 增强校验脚本
   - 检查每个插件的技能完整性
   - 检查 README / plugin.json / marketplace.json 一致性
   - 检查是否缺少 `customize` 等通用技能

3. 丰富参考资料
   - 增加更多法规、底稿模板、IT 审计检查清单
   - 增加更完整的中国审计准则索引

4. 产品化准备
   - 增加 LICENSE
   - 完善 ROADMAP / STATUS 文档
   - 增加示例案例与 demo 数据集

5. 集成验证
   - 对接真实 MCP 连接器（ERP / IAM / OA / 文档系统）
   - 在真实项目环境中回测技能实用性

## 贡献指南

本仓库的一切都是 Markdown 和 JSON。Fork 后编辑，提交 PR。

- 新技能 → 在对应插件的 `skills/` 下新建目录，编写 `SKILL.md`
- 新插件 → 新建插件目录，包含 `.claude-plugin/plugin.json`、`CLAUDE.md` 和 `skills/`
- 新连接器 → 在对应插件的 `.mcp.json` 中声明
- 提交前运行：

```bash
python3 scripts/validate.py
python3 scripts/lint-independence.py
```

## 相关文档

- `QUICKSTART.md` — 快速安装与首次运行
- `ARCHITECTURE.md` — 架构设计说明
- `CLAUDE.md` — 仓库开发规范
- `references/` — 共享参考资料

## License

当前仓库尚未补充正式 LICENSE 文件。建议下一步补齐。
