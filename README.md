# Claude for Audit

参考代理、技能和数据连接器，覆盖财务审计中最常见的工作流——法定审计、内部审计、合规审计、IT 审计、司法会计以及审计质量控制。

> **首次使用？** 从 [QUICKSTART.md](QUICKSTART.md) 开始——60 秒完成安装。这是完整参考手册。

> [!IMPORTANT]
> **本仓库所有输出均为审计人员的工作底稿草稿——不构成审计结论、鉴证意见或替代专业判断。** 每个技能均设有职业道德护栏：每项发现的来源标注、保守的默认假设、执业角色门控，以及关键输出前的复核节点。执业注册会计师（CPA）需对最终审计结论负责。这些技能让复核更快；不会替代它。
>
> **本仓库不代表普适的审计立场。** 审计准则、会计准则在不同行业和不同规模的企业适用性不同。使用本仓库的技能时，需要由承接该项目的执业 CPA 根据实际情况调整判断。

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
  deadline-monitor/         # 截止日监控
  anomaly-detector/         # 异常预警
references/                 # 共享参考资料
scripts/                    # 验证和部署脚本
```

## 设计原则

本仓库的设计融合了两个 Anthropic 官方参考仓库的最佳实践：

| 来源 | 借鉴点 |
|------|--------|
| **financial-services** | 金融领域专业计算技能、Excel 工作底稿生成、数据连接器（MCP） |
| **claude-for-legal** | Cold-start interview、Practice Profile、职业道德护栏、角色门控、定时 Agent |

### 核心设计理念

1. **一源双路（Two Ways from One Source）**——每个插件既可作为 Cowork 插件安装，也可通过 Managed Agent API 部署
2. **冷启动优先**——安装后先跑 cold-start-interview，采集事务所方法论，写入 Practice Profile
3. **零默认原则**——任何审计判断参数必须来自 Practice Profile，不预设默认值
4. **证据链完整性**——每个数字必须有来源、获取方式和审计程序索引
5. **发现 ≠ 结论**——所有输出标注“初步发现，需经复核”

## 插件列表

### 法定审计（statutory-audit）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/statutory-audit:cold-start-interview` | cold-start-interview | 采集事务所审计方法论，写入 Practice Profile |
| `/statutory-audit:risk-assessment` | risk-assessment | 风险评估程序——了解被审计单位及其环境 |
| `/statutory-audit:materiality` | materiality | 重要性水平确定——基准选择和计算 |
| `/statutory-audit:ic-review` | ic-review | 内部控制评价——了解、测试、评价 |
| `/statutory-audit:substantive-testing` | substantive-testing | 实质性程序——科目余额细节测试 |
| `/statutory-audit:sampling` | sampling | 审计抽样——统计/非统计抽样 |
| `/statutory-audit:confirmations` | confirmations | 函证程序——银行函证、往来款函证 |
| `/statutory-audit:journal-entry-testing` | journal-entry-testing | 日记账测试——异常分录识别 |
| `/statutory-audit:wp-generator` | wp-generator | 审计底稿生成——按底稿模板生成工作底稿 |
| `/statutory-audit:analytical-review` | analytical-review | 分析性复核——财务比率、趋势、波动分析 |
| `/statutory-audit:review-notes` | review-notes | 复核意见管理——项目组内部复核 |
| `/statutory-audit:report-drafting` | report-drafting | 审计报告草稿——无保留/保留/否定/无法表示意见 |

### 内部审计（internal-audit）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/internal-audit:audit-program` | audit-program | 审计方案制定——基于风险评估 |
| `/internal-audit:process-mapping` | process-mapping | 流程梳理——流程图、RACI |
| `/internal-audit:risk-control-matrix` | risk-control-matrix | 风险控制矩阵——风险→控制→测试 |
| `/internal-audit:data-analytics` | data-analytics | 数据分析——连续审计、异常检测 |
| `/internal-audit:finding-drafting` | finding-drafting | 审计发现——原因、影响、建议 |
| `/internal-audit:remediation-tracking` | remediation-tracking | 整改跟踪——整改进度、验证 |
| `/internal-audit:report-drafting` | report-drafting | 内审报告草稿 |

### 合规审计（compliance-audit）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/compliance-audit:regulatory-checker` | regulatory-checker | 法规检索与对照——适用的法规清单 |
| `/compliance-audit:pip-compliance` | pip-compliance | 个保法合规审查——数据分类、处理、跨境 |
| `/compliance-audit:anti-corruption` | anti-corruption | 反商业贿赂——FCPA / 中国反商业贿赂 |
| `/compliance-audit:tax-compliance` | tax-compliance | 税务合规——纳税申报、转让定价 |
| `/compliance-audit:sox-like` | sox-like | 内控合规评价——中国版 SOX |

### IT 审计（it-audit）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/it-audit:gc-attestation` | gc-attestation | 一般控制审计——安全、变更、逻辑访问 |
| `/it-audit:application-control` | application-control | 应用控制审计——输入、处理、输出控制 |
| `/it-audit:data-migration-audit` | data-migration-audit | 数据迁移审计——完整性、准确性 |
| `/it-audit:cybersecurity-review` | cybersecurity-review | 网络安全评价——等保 2.0 对标 |
| `/it-audit:caatt` | caatt | 计算机辅助审计技术——ACL、IDEA、Python |

### 司法会计（forensic-audit）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/forensic-audit:red-flags` | red-flags | 舞弊红旗识别 |
| `/forensic-audit:data-forensics` | data-forensics | 电子数据取证——日志、数据恢复 |
| `/forensic-audit:transaction-analysis` | transaction-analysis | 异常交易分析——关联方、循环交易 |
| `/forensic-audit:benford-analysis` | benford-analysis | 本福特定律检验——数字分布异常 |
| `/forensic-audit:whistleblower-triage` | whistleblower-triage | 举报线索分类——GR / YR / 三色分类 |

### 审计质量监控（audit-quality）

| 技能 | 命令 | 说明 |
|------|------|------|
| `/audit-quality:independence-check` | independence-check | 独立性检查——受禁服务、冷却期 |
| `/audit-quality:engagement-review` | engagement-review | 项目复核——三级复核制度 |
| `/audit-quality:peer-review` | peer-review | 同业互查——质量检查标准 |
| `/audit-quality:documentation-qc` | documentation-qc | 底稿质量控制——完整性、及时性 |
| `/audit-quality:ethics-screener` | ethics-screener | 职业道德筛查——利益冲突、保密 |

## 审计方法论

本仓库默认采用 **中国注册会计师审计准则（CSA）** 体系，同时支持 IFRS 和 ISA 框架。具体采用哪套准则在 cold-start-interview 中配置。

## 贡献指南

本仓库的一切都是 Markdown 和 JSON。Fork 后编辑，提交 PR。

- 新技能 → 在对应插件的 `skills/` 下新建目录，编写 `SKILL.md`
- 新插件 → `plugins/<name>/` 目录，包含 `.claude-plugin/plugin.json` 和 `skills/`
- 提交前运行 `python3 scripts/validate.py`

## License

[Apache License 2.0](./LICENSE)
