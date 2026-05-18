# Quickstart：60 秒安装

## 在 Claude Cowork 中安装

1. 打开 **Cowork** 标签
2. 点击左侧 **Customize**
3. 点击 **Browse plugins** → 添加本仓库 URL
4. 选择你需要的插件（至少安装 `statutory-audit`）

## 在 Claude Code 中安装

```bash
# 添加市场
claude plugin marketplace add <本仓库路径或URL>

# 安装核心插件——法定审计
claude plugin install statutory-audit@claude-for-audit

# 按需安装其他
claude plugin install internal-audit@claude-for-audit
claude plugin install compliance-audit@claude-for-audit
```

## 首次配置

安装完成后，**第一件事**是跑冷启动采访：

```bash
/statutory-audit:cold-start-interview
```

> ⚠️ **冷启动采访不是可选的。** 在完成冷启动之前，所有技能都会拒绝执行实质性工作。采访会问大约 10-15 分钟的问题——事务所信息、方法论偏好、底稿格式——然后写入一份专属的 Practice Profile。这个 profile 是所有技能运行的依据。

### 快速开始 vs 完整采访

- **快速开始（~2 分钟）**：只问基本信息，用通用审计模板。适合先快速体验。
- **完整采访（~15 分钟）**：读你的审计方法论文档、历史底稿、事务所内部规范。输出更贴合实际工作。
- 完整采访随时可以补跑：`/statutory-audit:cold-start-interview --redo`

## 测试运行

配置完成后，上传你的试算表和科目余额表：

```bash
# 风险评估
/statutory-audit:risk-assessment

# 确定重要性水平
/statutory-audit:materiality

# 生成实质性程序底稿
/statutory-audit:wp-generator

# 分析性复核
/statutory-audit:analytical-review
```

## 连接数据源

在 `~/.claude/plugins/config/claude-for-audit/statutory-audit/.mcp.json` 中配置：

| 连接器 | 配置方式 |
|-------|---------|
| 企业 ERP（用友/金蝶） | 添加 MCP URL 和 API Key |
| 银行流水 | 配置银行接口 |
| 企查查/天眼查 | 配置 API Token |
| 企业网盘/飞书 | OAuth 授权 |

## 下一步

- 完整阅读 [README.md](README.md) 了解所有插件
- 查看 [ARCHITECTURE.md](ARCHITECTURE.md) 了解设计原理
- 阅读对应插件的 `README.md` 了解具体技能