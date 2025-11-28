import requests

from domain.llmconfig import LLMConfig


class OpenRouterLLMProvider:
    def __init__(
        self, config: LLMConfig, session: requests.Session | None = None
    ) -> None:
        self._config = config
        self._session = session or requests.Session()

    def execute(self, text: str) -> tuple[str, int]:
        """
        text — уже подготовленный промпт (включая "системные" инструкции в тексте)
        """

        headers = {
            'Authorization': f'Bearer {self._config.api_key}',
            'Content-Type': 'application/json',
        }

        body = {
            'model': self._config.model,
            'messages': [
                # {'role': 'system', 'content': self._config.system_prompt},
                {'role': 'user', 'content': self._config.system_prompt + text},
            ],
            'temperature': self._config.temperature,
            'top_p': self._config.top_p,
            'max_tokens': self._config.max_tokens,
        }

        resp = self._session.post(
            self._config.base_url,
            headers=headers,
            json=body,
            timeout=self._config.timeout,
        )
        resp.raise_for_status()
        data = resp.json()

        # OpenRouter возвращает OpenAI-совместное тело: choices + usage
        # choices[0].message.content текст ответа, usage.total_tokens токены
        content = data['choices'][0]['message']['content']
        tokens = data.get('usage', {}).get('total_tokens', 0)

        return content, tokens
