"""单元测试（Day 4 实现）。

关键手法：mock 掉模型响应，测试不烧真 API、不依赖网络，
几毫秒跑完——这是 CI 能每次 push 都跑的前提。

面试可讲：工具函数单测 + 循环终止条件测试 + mock 隔离外部依赖。
"""

import json
from unittest.mock import MagicMock, patch

from jd_match_agent import agent as agent_module


def test_extract_requirements_valid_jd():
    """给定一段 JD，应返回包含 hard_skills 的字典（Day 4 实现）。

    提示：patch jd_match_agent.tools 里创建 client 的位置，
    让 fake client 的 chat.completions.create 返回一个 MagicMock，
    其 choices[0].message.content 是一段 JSON 字符串。
    """
    raise NotImplementedError("Day 4 实现")


def test_agent_loop_terminates_on_text_reply():
    """模型直接输出文本时，循环应立刻返回、不进入下一轮（Day 4 实现）。

    提示：mock run_agent 里 client.chat.completions.create 的返回值，
    让 choices[0].message.tool_calls 为空、content 为 "最终报告"，
    断言 run_agent(...) 返回 "最终报告"，且 create 只被调用了 1 次。
    """
    raise NotImplementedError("Day 4 实现")


def test_agent_loop_respects_max_iterations():
    """模型一直要求调工具时，循环应在 max_iterations 后强制终止（Day 4 实现）。

    提示：让 mock 的 tool_calls 永远非空，断言返回兜底文案，
    且 create 的调用次数等于 settings.max_iterations。
    """
    raise NotImplementedError("Day 4 实现")
