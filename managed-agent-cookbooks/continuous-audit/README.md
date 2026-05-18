# Continuous Audit — managed-agent template

持续审计监控代理——定期从企业 ERP 获取财务数据，运行异常检测规则，并在发现异常时发送预警。

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export ERP_MCP_URL=...
scripts/deploy-managed-agent.sh continuous-audit
```

## 运营

- 默认频率：每周一自动运行
- 输出：异常预警报告 → 指定的消息通道
- 连接器：企业 ERP MCP + Slack/Messaging MCP

## Security

持续审计代理只读访问 ERP 系统，没有写权限。所有发现输出为预警通知，不生成底稿。