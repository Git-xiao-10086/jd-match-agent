"""Agent 主循环（Day 3 实现，全程最硬的一天）。

这就是"最小企业级 Agent"的心脏。原理只有三步，面试必考：
  1. 模型看到工具列表，决定调哪个工具（输出结构化 JSON，即 tool_calls）
  2. 运行时解析这个 JSON，真正执行函数
  3. 执行结果回填进 messages，模型基于结果继续推理
重复直到模型不再要求调工具（直接输出终稿）或达到 max_iterations。

实现提示：照下面的伪代码逐行翻译成 Python 即可。卡住了就问我，
这天崩了别怀疑自己，裸写循环对零基础本来就是硬仗。
"""

from openai import OpenAI

from jd_match_agent.config import settings
from jd_match_agent.tools import TOOL_SCHEMAS, execute_tool

SYSTEM_PROMPT = """你是求职匹配分析 Agent。你的任务：分析用户提供的招聘 JD 和简历，
按以下顺序调用工具：
1. extract_requirements 提取 JD 技能清单
2. match_resume 比对简历
3. generate_report 生成差距报告
每一步基于上一步的结果决策，不要跳过。拿到报告后直接输出给用户。"""


def run_agent(jd_text: str, resume_text: str) -> str:
    """跑一次完整的 JD 匹配分析，返回最终报告文本。

    伪代码（Day 3 逐行实写）：

        client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"JD: {jd_text}\n\n简历: {resume_text}"},
        ]

        for i in range(settings.max_iterations):        # 防死循环
            response = client.chat.completions.create(
                model=settings.model_name,
                messages=messages,
                tools=TOOL_SCHEMAS,                     # 告诉模型有哪些工具
            )
            message = response.choices[0].message

            if message.tool_calls:                      # 模型要调工具
                messages.append(message)                # 模型的决策也要进上下文
                for call in message.tool_calls:
                    result = execute_tool(call.function.name, call.function.arguments)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": call.id,        # 必须回填，否则报错
                        "content": result,              # 执行结果回填
                    })
            else:                                       # 模型直接输出 = 任务完成
                return message.content

        return "达到最大迭代次数，强制终止"               # 兜底，绝不无限循环
    """
    raise NotImplementedError("Day 3 实现：按 docstring 中的伪代码逐行翻译")
