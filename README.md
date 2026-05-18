# Claude for Audit

面向中国审计与合规场景的 Claude 插件仓库，覆盖财务审计中最常见的工作流——法定审计、内部审计、合规审计、IT 审计、司法会计以及审计质量控制。

> 首次使用？从 `QUICKSTART.md` 开始。
>
> 当前状态：六大核心插件已全部落地，仓库校验状态为 `✅ 全部检查通过`。

[!IMPORTANT]
本仓库所有输出均为审计人员的工作底稿草稿，不构成审计结论、鉴证意见、监管结论或替代专业判断。每个技能均设有职业道德护栏：来源标注、角色门控、整改闭环、复核节点和独立性约束。最终判断仍由具备授权的专业人员负责。

## 当前已实现状态

- 6 个核心插件全部建成
- 49 个技能已落地
- 7 个最小代理已落地
- 统一的 Practice Profile 机制已建立
- 统一的校验脚本、状态文档和许可证已建立

### 完成度总览

| 插件 | 状态 | 技能数 | 代理数 | 说明 |
|------|------|--------|--------|------|
| `statutory-audit` | 已实现 | 13 | 1 | 法定审计主流程完整 |
| `internal-audit` | 已实现 | 9 | 2 | 内审项目与整改闭环完整 |
| `compliance-audit` | 已实现 | 7 | 1 | 合规审计主线完整 |
| `it-audit` | 已实现 | 7 | 1 | IT 审计核心域完整 |
| `forensic-audit` | 已实现 | 7 | 1 | 舞弊调查与取证完整 |
| `audit-quality` | 已实现 | 7 | 1 | 质量控制约束层完整 |

## 快速导航

- `QUICKSTART.md` — 安装与首次运行
- `ARCHITECTURE.md` — 架构设计说明
- `STATUS.md` — 当前进度与待办
- `DEMO.md` — 六大插件最小演示路径
- `references/` — 共享参考资料

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
references/                 # 共享参考资料
scripts/                    # 验证和部署脚本
```

## 设计原则

本仓库融合了两个 Anthropic 官方参考仓库的最佳实践：

| 来源 | 借鉴点 |
|------|--------|
| `financial-services` | 专业技能、结构化产出、数据连接器（MCP） |
| `claude-for-legal` | Cold-start interview、Practice Profile、角色门控、定时 Agent |

### 核心理念

1. 一源双路（插件 + Managed Agent）
2. 冷启动优先（Practice Profile 先于技能运行）
3. 零默认原则（参数从团队方法论中来）
4. 证据链完整性（结论可追溯）
5. 发现 ≠ 结论（默认初步发现）
6. 质量约束前置（`audit-quality` 作为横向控制层）

## 插件摘要

### `statutory-audit`
- 风险评估、重要性、控制测试、实质性程序、抽样、函证、分析性复核、底稿生成、复核、报告起草
- Agent：`deadline-watcher`

### `internal-audit`
- 审计方案、流程梳理、风险控制矩阵、数据分析、审计发现、整改跟踪、报告起草
- Agents：`continuous-monitor`、`finding-follow-up`

### `compliance-audit`
- 法规适用、个保法、反商业贿赂、税务合规、SOX-like 内控合规评价
- Agent：`policy-monitor`

### `it-audit`
- ITGC、应用控制、数据迁移、网络安全、CAATT
- Agent：`control-monitor`

### `forensic-audit`
- 红旗识别、本福特定律、异常交易分析、电子取证、举报线索三色分类
- Agent：`case-watch`

### `audit-quality`
- 独立性检查、项目复核、同业互查、底稿质控、职业道德筛查
- Agent：`quality-watch`

## 当前定位

当前版本更接近：
- 可维护的仓库蓝图
- 可运行的插件原型集
- 团队内部工具与方法论承载层

尚不是：
- 已对接真实客户环境的成熟商用产品
- 已绑定具体厂商连接器的交付版本

## 下一步方向

1. 增加 demo 数据集和示例案例
2. 对接真实 MCP 连接器（ERP / OA / IAM / SIEM / 文档系统）
3. 补充更多 references 和输出模板
4. 增强 managed-agent-cookbooks

## 贡献指南

提交前运行：

```bash
python3 scripts/validate.py
python3 scripts/lint-independence.py
```

## License

见 `LICENSE`（Apache 2.0）
