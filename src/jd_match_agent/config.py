"""配置加载（Day 1-2 使用）。

所有配置从环境变量 / .env 文件读取，密钥绝不硬编码、绝不提交 Git。
这是 FDE JD 里"数据安全与权限控制"的最小实践。
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """从 .env 读取的配置项。

    用法（Day 2 起）：
        from jd_match_agent.config import settings
        client = OpenAI(api_key=settings.api_key, base_url=settings.base_url)
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ---- Day 2 填写：模型 API ----
    # 选 DeepSeek 或智谱 GLM，二选一，把对应的 key 填进 .env
    api_key: str = ""            # .env 中: API_KEY=sk-xxx
    base_url: str = ""           # DeepSeek: https://api.deepseek.com
                                 # 智谱:   https://open.bigmodel.cn/api/paas/v4
    model_name: str = ""         # DeepSeek: deepseek-chat / 智谱: glm-4

    # ---- Day 5 使用：服务与日志 ----
    log_level: str = "INFO"
    max_iterations: int = 10     # Agent 循环最大轮数，防死循环


settings = Settings()
