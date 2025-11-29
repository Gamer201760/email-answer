from usecase.interface import LLMProviderRepository
from rag.rag import get_context

class AnswerUsecase:
    def __init__(
        self,
        agent: LLMProviderRepository,
    ) -> None:
        self._agent = agent

    def execute(self, text: str) -> tuple[str, int]:
        return self._agent.execute(text)

    def answer(self, text: str) -> tuple[str, int]:
        # 2. RAG КОНТЕКСТ (1 строка!)
        context = get_context(text, k=3)
        
        # 3. ПРОМПТ С КОНТЕКСТОМ
        prompt = f"""📚 ПРАВИЛА БАНКА ИЗ ДОКУМЕНТОВ:
{context}

👤 ЗАПРОС КОЛЛЕГИ: {text}

📝 Ответь ОФИЦИАЛЬНО, указав:
1. Можно ли выполнить запрос
2. СРОКИ по правилам 
3. Необходимые действия
4. Ссылку на документ (если есть)

Тон: деловой, строгий, по правилам банка."""

        return self._agent.execute(prompt)