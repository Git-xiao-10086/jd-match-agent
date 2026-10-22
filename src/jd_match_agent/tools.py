"""工具层（Day 2-3 实现）。

三个工具函数 + 对应的 tool schema（告诉模型每个工具干什么、参数是什么）。
先写普通函数跑通逻辑，再补 schema 包装——第 3 天主循环按 schema 调模型。

注意：函数体留空，核心逻辑由你自己写。docstring 里是实现提示，
写完后能对着讲清楚每一步，面试才不慌。
"""

import json

# ============================================================
# Day 2：extract_requirements
# ============================================================


def extract_requirements(jd_text: str) -> dict:
    """从 JD 文本中提取技能要求，分为硬性技能 / 软素质 / 加分项三类。

    输入：JD 全文文本
    输出：{"hard_skills": [...], "soft_skills": [...], "bonus_skills": [...]}

    实现提示（Day 2）：
    1. 构造 messages：system 定义角色，并明确要求"只输出 JSON，
       格式为 {...}"；user 放 JD 文本。
    2. 调 client.chat.completions.create，response_format={"type": "json_object"}。
    3. json.loads 解析返回的 content，校验三个字段存在，返回 dict。
    """
    raise NotImplementedError("Day 2 实现：按 docstring 的三步提示写")


# ============================================================
# Day 3：match_resume
# ============================================================


def match_resume(skills: dict, resume_text: str) -> dict:
    """把 JD 技能清单与简历文本逐条比对。

    输入：extract_requirements 的输出 + 简历全文
    输出：{"matched": [{"skill": "...", "evidence": "简历中的对应描述"}],
           "missing": ["..."]}

    实现提示（Day 3）：
    1. 遍历 skills 的三个列表，逐条让模型判断简历中是否有对应证据。
    2. 有证据 → matched 并摘录原文句子；无证据 → missing。
    3. 也可以一次性把 skills JSON + resume 都塞给模型，让它直接输出比对结果
       （更快，但 prompt 要写清楚输出格式）。
    """
    raise NotImplementedError("Day 3 实现：按 docstring 提示写")


# ============================================================
# Day 3：generate_report
# ============================================================


def generate_report(matches: dict) -> str:
    """把比对结果汇总成 Markdown 差距分析报告。

    输入：match_resume 的输出
    输出：Markdown 字符串（含匹配项、缺口项、投递建议三节）

    实现提示（Day 3）：
    1. 纯字符串拼接即可，不调模型——工具不一定都要调 LLM，
       确定性逻辑用代码更稳（这点面试可以讲）。
    2. 报告末尾给一句总结论：匹配度百分比 + 最该补的三项。
    """
    raise NotImplementedError("Day 3 实现：按 docstring 提示写")


# ============================================================
# Day 3：tool schemas —— 告诉模型有哪些工具、怎么调
# ============================================================

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "extract_requirements",
            "description": "从招聘 JD 文本中提取技能要求，分硬性技能/软素质/加分项三类",
            "parameters": {
                "type": "object",
                "properties": {
                    "jd_text": {"type": "string", "description": "招聘 JD 全文"},
                },
                "required": ["jd_text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "match_resume",
            "description": "把 JD 技能清单与简历文本逐条比对，输出匹配项与缺口项",
            "parameters": {
                "type": "object",
                "properties": {
                    "skills": {"type": "object", "description": "extract_requirements 的输出"},
                    "resume_text": {"type": "string", "description": "简历全文"},
                },
                "required": ["skills", "resume_text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "generate_report",
            "description": "把比对结果汇总成 Markdown 差距分析报告",
            "parameters": {
                "type": "object",
                "properties": {
                    "matches": {"type": "object", "description": "match_resume 的输出"},
                },
                "required": ["matches"],
            },
        },
    },
]

# 工具名 → 函数 的分发表，Day 3 主循环用它执行 tool_calls
TOOL_FUNCTIONS = {
    "extract_requirements": extract_requirements,
    "match_resume": match_resume,
    "generate_report": generate_report,
}


def execute_tool(name: str, arguments_json: str):
    """主循环调用入口：解析 JSON 参数并执行对应工具。

    Day 3 已为你写好（这是机制，不是业务逻辑）：
    1. 从 TOOL_FUNCTIONS 取出函数（查不到就报错返回，防止模型幻觉工具名）。
    2. json.loads 解析 arguments_json。
    3. 调用函数，结果 json.dumps 成字符串返回（工具结果必须回填为字符串）。
    """
    func = TOOL_FUNCTIONS.get(name)
    if func is None:
        return json.dumps({"error": f"unknown tool: {name}"}, ensure_ascii=False)
    try:
        kwargs = json.loads(arguments_json)
    except json.JSONDecodeError as e:
        return json.dumps({"error": f"invalid arguments: {e}"}, ensure_ascii=False)
    result = func(**kwargs)
    if isinstance(result, str):
        return result
    return json.dumps(result, ensure_ascii=False)
