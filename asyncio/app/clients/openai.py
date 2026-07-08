from openai import AsyncOpenAI
import time

from app.config import OPENAI_API_KEY
from app.models import ModelResponse

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def ask_openai(prompt: str) -> ModelResponse:

    start = time.perf_counter()

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    latency = time.perf_counter() - start

    return ModelResponse(
        provider="OpenAI",
        response=response.choices[0].message.content,
        latency=latency,
        success=True,
    )