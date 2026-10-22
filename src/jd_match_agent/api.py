"""FastAPI 服务化（Day 5 实现）。

把 Day 3 跑通的终端程序包成 HTTP 服务——这一步是 Agent 开发与 FDE 部署的
交集：Agent 岗看接口设计，FDE 岗看服务启停与日志排查。
"""

import uuid

from fastapi import FastAPI

from jd_match_agent.config import settings

app = FastAPI(title="JD-Match Agent", version="0.1.0")


@app.get("/health")
def health():
    """健康检查（Day 5 已可用，部署时探活用）。"""
    return {"status": "ok"}


@app.post("/analyze")
def analyze(jd_text: str, resume_text: str):
    """分析接口（Day 5 实现）。

    实现提示：
    1. 入参用 pydantic BaseModel 校验（jd_text/resume_text 非空、长度上限）。
    2. 生成请求 ID：request_id = str(uuid.uuid4())[:8]，
       之后每条日志都带它——一条请求从进来到出报告整条可串（可观测性）。
    3. 调 run_agent(jd_text, resume_text)，把最终报告放进响应体，
       响应里带上 request_id 和耗时。
    """
    raise NotImplementedError("Day 5 实现：按 docstring 的三步提示写")
