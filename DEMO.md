# DEMO

本文件给出 `claude-for-audit` 的最小演示路径，帮助新使用者快速理解 6 大插件如何落地。

## 一、法定审计最小演示路径

适用场景：
- 一家制造业公司 2024 年度财务报表审计
- 目标：从冷启动到报告草稿跑通一条主链路

建议顺序：

1. `/statutory-audit:cold-start-interview`
   - 录入事务所方法论、重要性水平偏好、底稿编码、复核结构

2. `/statutory-audit:risk-assessment`
   - 识别重大错报风险、舞弊风险、关键审计事项

3. `/statutory-audit:materiality`
   - 计算 PM / TE / SAD

4. `/statutory-audit:analytical-review`
   - 先做整体波动分析和异常识别

5. `/statutory-audit:substantive-testing --revenue`
   - 针对高风险收入执行实质性程序

6. `/statutory-audit:confirmations`
   - 跑银行函证或往来款函证

7. `/statutory-audit:wp-generator`
   - 汇总生成底稿包

8. `/statutory-audit:review-notes`
   - 完成三级复核记录

9. `/statutory-audit:report-drafting`
   - 生成审计报告草稿

## 二、内部审计最小演示路径

适用场景：
- 对采购到付款流程开展内审

建议顺序：

1. `/internal-audit:cold-start-interview`
2. `/internal-audit:audit-program`
3. `/internal-audit:process-mapping`
4. `/internal-audit:risk-control-matrix`
5. `/internal-audit:data-analytics`
6. `/internal-audit:finding-drafting`
7. `/internal-audit:report-drafting`
8. `/internal-audit:remediation-tracking`

## 三、合规审计最小演示路径

适用场景：
- 对 APP 用户信息收集合规进行专项审查

建议顺序：

1. `/compliance-audit:cold-start-interview`
2. `/compliance-audit:regulatory-checker`
3. `/compliance-audit:pip-compliance`
4. 如涉及第三方营销或渠道 → `/compliance-audit:anti-corruption`
5. 输出整改建议并纳入台账

## 四、IT 审计最小演示路径

适用场景：
- 审查 ERP 所在 IT 环境是否可信

建议顺序：

1. `/it-audit:cold-start-interview`
2. `/it-audit:gc-attestation`
3. `/it-audit:application-control`
4. 如有系统切换 → `/it-audit:data-migration-audit`
5. 如有安全基线需求 → `/it-audit:cybersecurity-review`
6. 批量分析补充 → `/it-audit:caatt`

## 五、司法会计最小演示路径

适用场景：
- 收到匿名举报，怀疑采购回扣

建议顺序：

1. `/forensic-audit:cold-start-interview`
2. `/forensic-audit:whistleblower-triage`
3. `/forensic-audit:red-flags`
4. `/forensic-audit:transaction-analysis`
5. 如需电子证据固定 → `/forensic-audit:data-forensics`
6. 如需辅助统计分析 → `/forensic-audit:benford-analysis`

## 六、审计质量最小演示路径

适用场景：
- 年度质量检查/重点项目 EQCR

建议顺序：

1. `/audit-quality:cold-start-interview`
2. `/audit-quality:independence-check`
3. `/audit-quality:engagement-review`
4. `/audit-quality:documentation-qc`
5. `/audit-quality:ethics-screener`
6. 批量抽查项目时 → `/audit-quality:peer-review`

## 七、代理（Agent）演示路径

可周期性运行的最小代理：

- `statutory-audit/agents/deadline-watcher.md`
- `internal-audit/agents/continuous-monitor.md`
- `internal-audit/agents/finding-follow-up.md`
- `compliance-audit/agents/policy-monitor.md`
- `it-audit/agents/control-monitor.md`
- `forensic-audit/agents/case-watch.md`
- `audit-quality/agents/quality-watch.md`

## 八、推荐的真实验证顺序

如果要做第一次真实项目验证，建议按以下顺序：

1. `statutory-audit`
2. `audit-quality`
3. `internal-audit`
4. `compliance-audit`
5. `it-audit`
6. `forensic-audit`

原因：
- 法定审计最容易定义起点和终点
- 质量插件可作为横向约束层同步验证
- 内审和合规更适合在企业内部落地
- IT 与司法会计对连接器和证据环境要求更高
