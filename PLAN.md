# JD-Match Agent — 10 天冲刺计划

目标：2026 年 11 月初投递寒假实习前，产出一个能撑住面试深挖的简历项目
方向：Agent 开发（主攻）+ FDE 部署（平行投递线）
节奏：每天 5-6 小时，主体 7 天完成，第 8-10 天做简历与面试弹药

---

## 一、策略总纲

1. 倒排法：简历写什么 → 面试问什么 → 项目做什么 → 学什么。不按教程正排，正排必然来不及。
2. 一个项目命中两个方向。基于真实 JD 交叉验证的能力交集：Python 工程能力 + Function Calling 原理 + FastAPI 服务化 + Docker 部署 + Git 分支管理 + 测试与文档沉淀。
3. FDE 实习坑位少，简历主投 Agent 岗；把部署能力写成项目的差异化亮点，FDE 岗平行投递，面试话术："我理解 FDE 是把技术落到客户现场最后一公里，我的项目自己完成了容器化交付全流程。"

## 二、技术栈与选型理由

- 包管理：uv。一条命令管 Python 版本 + 虚拟环境 + 依赖，比 pip + venv 现代，且是简历上的工具链亮点。
- 语言：Python 3.12。
- 模型 API：DeepSeek 或智谱 GLM。OpenAI 兼容格式，充十几块够整个项目。密钥走 .env，绝不硬编码、绝不提交 Git。
- Agent 形态：裸写 ReAct 循环 + Function Calling，不用 LangChain。框架是糖，原理是骨——面试问"Function Calling 怎么实现的"，自己写过循环的人才能讲清"模型输出结构化 JSON → 运行时解析执行 → 结果回填上下文"这三步。
- 服务化：FastAPI（/analyze + /health，pydantic 校验）。
- 部署：Docker 多阶段构建 + docker-compose 一键起服务。
- 质量：pytest（单测 + mock 模型响应）+ ruff（lint）+ GitHub Actions（push 触发流水线）。

## 三、项目设计：JD-Match Agent

输入一段招聘 JD 文本和你的简历文本，Agent 自主完成：提取技能要求 → 区分硬性/加分项 → 与简历比对 → 输出匹配度差距报告（Markdown）。

工具层设计（先做前三个，第四个是扩展点）：

1. `extract_requirements(jd_text)` — 从 JD 提取技能清单，输出 `{"hard_skills": [...], "soft_skills": [...], "bonus_skills": [...]}`。
2. `match_resume(skills, resume_text)` — 技能与简历比对，输出各技能匹配状态与证据。
3. `generate_report(matches)` — 汇总生成 Markdown 差距分析报告。
4. `analyze_github_repo(repo_url)`（第 7 天若提前完成再加）— 调 GitHub API 分析仓库技术栈与活跃度，作为简历上的扩展点。

Agent 主循环的伪代码见 `src/jd_match_agent/agent.py` 的 docstring，第 3 天照着实写。

## 四、10 天逐日计划

### Day 1（约 4h）工程环境 + Git 首秀
- 装 uv；建 GitHub 仓库 jd-match-agent；把现有骨架文件 push 上去。
- 所有改动走功能分支 + PR，commit 用 feat/fix/docs/test/refactor 前缀。
- 验收：GitHub 上能看到带 README 的项目，提交历史干净；.env 已被 .gitignore 屏蔽。

### Day 2（约 5-6h）API 跑通 + 第一个工具
- 注册 DeepSeek 或智谱，充值，key 写入 .env。
- 写脚本跑通第一个 chat completion，搞懂 messages 角色结构和 tool_calls 字段。
- 实现 `extract_requirements`，终端粘贴真实 JD 能打印结构化技能清单。
- 验收：终端输出分类正确的技能 JSON。

### Day 3（约 5-6h）ReAct 主循环（全程最硬的一天）
- 按 agent.py 中的伪代码实写循环：带工具列表调模型 → 有 tool_calls 就执行并回填 messages → 没有就输出终稿。
- max_iterations=10 防死循环。补齐 `match_resume` 和 `generate_report`。
- 验收：JD + 真实简历一起输入，终端输出完整差距报告。
- 心理准备：裸写循环对零基础本来就是硬仗，这天崩了别怀疑自己，卡住就问我。

### Day 4（约 4-5h）测试与代码质量
- pytest 单测覆盖三个工具函数和循环终止逻辑（mock 假造模型响应，不烧真 API）。
- ruff 全量 lint，类型注解补全。
- 验收：pytest 全绿，ruff check 零警告。

### Day 5（约 5-6h）FastAPI 服务化
- /analyze 接口（pydantic 模型校验入参）+ /health。
- 结构化日志带请求 ID：一条请求从进来到出报告能整条串起来（简历话术：可观测性）。
- 验收：uvicorn 起服务，curl 调一次完整分析，日志可见全链路。

### Day 6（约 5-6h）Docker + CI
- Dockerfile 多阶段构建 + docker-compose 一键起服务，容器内验证接口。
- GitHub Actions：push 触发 ruff + pytest。
- 验收：README 出现绿色 CI 徽章，docker compose up 一条命令起服务。

### Day 7（约 4-5h）README + 收尾
- README 四节：项目简介、mermaid 架构图、快速开始（陌生人 5 分钟跑起来）、设计取舍（这节就是面试答案库）。
- 若提前完成，加 `analyze_github_repo` 扩展工具。
- 验收：按自己的 README 在干净环境完整跑通一次。

### Day 8 简历
- 项目段按 STAR 写两个版本：Agent 岗版突出工具编排与 Prompt 设计；FDE 岗版突出容器化交付与日志排查。见第六节模板。

### Day 9 面试弹药
- 把第七节八个问题写成自己的答案，每条用项目真实细节作答。

### Day 10 缓冲 + 投递清单
- 补任何未通过的验收缺口；整理投递清单（公司、岗位、截止日期、渠道）。

## 五、Git 最小生存包

不单独学 Git，命令嵌在项目过程中用，用两次就记住了。全集就这些：`init`、`clone`、`status`、`diff`、`add`、`commit`、`push`、`checkout -b`、`checkout`、`log`，加一个 `.gitignore`。分支策略一条：main 只放可用代码，所有改动走功能分支 + PR（单人项目也走，FDE JD 明确看这个）。

## 六、简历项目描述模板（STAR）

- Agent 岗版：针对求职季 JD 筛选效率低的问题，独立设计并实现基于 Function Calling 的 ReAct 智能体服务：封装 JD 解析、简历匹配、报告生成 3 个工具，实现多轮工具调用编排与死循环防护；通过 FastAPI 服务化暴露 API，结构化日志支持全链路请求追踪。
- FDE 岗版：同一项目改用交付视角表述——Docker Compose 一键部署、GitHub Actions 自动化 lint 与测试、配置与密钥分离（.env + pydantic-settings）、容器内接口验证与日志排查实践。

注意：全是动作和数字，没有"学习了""了解了"。

## 七、面试八问（Day 9 写成自己的答案）

1. 你的 Agent 和直接问模型有什么区别？
2. Function Calling 的原理是什么？
3. 为什么不用 LangChain？
4. Agent 死循环怎么防？
5. 怎么保证输出稳定性（重试、schema 校验、prompt 版本管理）？
6. Docker 部署踩过什么坑（依赖版本、镜像瘦身、时区）？
7. CI 里跑了什么？
8. 请求日志怎么做到全链路追踪？

## 八、风险与取舍

1. 10 天做不出"企业级"，只做得出"工程习惯达标的实习生项目"——简历和面试都这么说自己，说大了面试一问就穿，诚实反而是加分项。
2. Python 零基础上工程栈会挫败，允许抄官方文档和模板，抄懂就行，抄完能讲出来就是你的。
3. 如果 Day 9 还没做完，砍工具数量保完成度。面试官看"做完了 + 讲得清"，不是功能数。
