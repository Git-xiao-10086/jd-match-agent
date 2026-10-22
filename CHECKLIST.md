# JD-Match Agent — 每日勾选清单

每天完工后对照验收标准打勾。没打勾的天数不往后赶，先补缺口——完成度 > 进度。

## Day 1 — 工程环境 + Git 首秀 ✅ 2026-10-22 完成
- [x] uv 安装成功（uv --version 有输出）
- [x] GitHub 仓库 jd-match-agent 建好（Git-xiao-10086/jd-match-agent）
- [x] 骨架文件已 push：README、pyproject.toml、.gitignore、src/、tests/
- [x] .env 被 .gitignore 屏蔽（git status 不出现 .env）
- [x] 提交历史干净，commit message 带 feat/fix/docs 前缀
验收：陌生人打开 GitHub 能看到带 README 的项目。

## Day 2 — API 跑通 + 第一个工具
- [ ] DeepSeek / 智谱账号注册并充值
- [ ] API key 写入 .env（未提交 Git）
- [ ] 第一个 chat completion 脚本跑通，看清了 tool_calls 字段结构
- [ ] extract_requirements 实现完成
验收：终端粘贴真实 JD，打印出分类正确的技能 JSON。

## Day 3 — ReAct 主循环（最硬的一天）
- [ ] 主循环按 agent.py 伪代码实写完成
- [ ] max_iterations 防护生效
- [ ] match_resume 实现完成
- [ ] generate_report 实现完成
验收：JD + 真实简历输入，终端输出完整差距报告。

## Day 4 — 测试与代码质量
- [ ] pytest 覆盖三个工具函数
- [ ] 循环终止逻辑有 mock 测试
- [ ] ruff check 零警告
- [ ] 类型注解补全
验收：pytest 全绿，ruff 零警告。

## Day 5 — FastAPI 服务化
- [ ] /analyze 接口 + pydantic 入参校验
- [ ] /health 健康检查
- [ ] 结构化日志带请求 ID
验收：uvicorn 起服务，curl 完整分析一次，日志可见全链路。

## Day 6 — Docker + CI
- [ ] Dockerfile 多阶段构建
- [ ] docker-compose 一键起服务
- [ ] 容器内接口验证通过
- [ ] GitHub Actions 配好（push 触发 ruff + pytest）
验收：README 有绿色 CI 徽章，docker compose up 起服务。

## Day 7 — README + 收尾
- [ ] README 四节写全（简介 / 架构图 / 快速开始 / 设计取舍）
- [ ] （扩展项）analyze_github_repo 工具
- [ ] 按 README 在干净环境完整跑通一次
验收：陌生人 clone 后 5 分钟跑起来。

## Day 8 — 简历
- [ ] Agent 岗版项目描述（STAR）
- [ ] FDE 岗版项目描述（STAR）

## Day 9 — 面试弹药
- [ ] 面试八问逐条写成自己的答案

## Day 10 — 缓冲 + 投递清单
- [ ] 补齐未通过的验收缺口
- [ ] 投递清单整理完（公司 / 岗位 / 截止日期 / 渠道）
