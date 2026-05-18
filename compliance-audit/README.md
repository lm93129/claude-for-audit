# 合规审计插件（compliance-audit）

覆盖中国常见合规审计场景——法规检索、个人信息保护法合规、反商业贿赂、税务合规、内控评价。

## 技能速查

| 命令 | 说明 |
|------|------|
| `/compliance-audit:cold-start-interview` | 冷启动采访 |
| `/compliance-audit:regulatory-checker` | 法规检索与适用性分析 |
| `/compliance-audit:pip-compliance` | 个保法（PIPL）合规审查 |
| `/compliance-audit:anti-corruption` | 反商业贿赂合规审计 |
| `/compliance-audit:tax-compliance` | 税务合规审计 |
| `/compliance-audit:sox-like` | 内控合规评价 |

## 设计特点

- 以中国监管语境为主：个保法、数据安全法、反不正当竞争法、税收征管法等
- 输出面向内部整改和管理层治理，不直接形成对外鉴证结论
- 每项结论必须给出法规依据、制度依据、证据来源和整改优先级
