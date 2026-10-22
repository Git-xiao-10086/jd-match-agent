# JD-Match Agent

> 基于 Function Calling 的 ReAct 智能体服务 —— 输入招聘 JD 与简历文本，自主完成技能提取、匹配度分析与差距报告生成。

## 状态

开发中（2026-10-22 启动，10 天冲刺计划见 PLAN.md，每日进度见 CHECKLIST.md）。

## 架构

<!-- Day 7 替换为 mermaid 图 -->

输入（JD + 简历）→ ReAct 循环（LLM 决策调哪个工具）→ 工具层（3 个工具）→ Markdown 差距报告
服务化：FastAPI 暴露 /analyze，Docker Compose 一键部署，GitHub Actions 自动 lint + test

## 快速开始

<!-- Day 7 补全，目标：陌生人 clone 后 5 分钟跑起来 -->

```bash
uv sync                          # 安装依赖
cp .env.example .env             # 填入 API Key
uv run uvicorn jd_match_agent.api:app --reload
```

## 设计取舍

<!-- Day 7 补全，这一节就是面试答案库 -->

- 为什么裸写 ReAct 循环而不用 LangChain
- 死循环防护：max_iterations
- 配置与密钥分离：.env + pydantic-settings
- 可观测性：请求 ID 串联全链路日志
