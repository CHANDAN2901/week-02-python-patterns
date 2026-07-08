from openai import AsyncOpenAI
import time

from app.config import OPENROUTER_API_KEY
from app.models import ModelResponse

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


async def ask_openrouter(prompt: str):

    start = time.perf_counter()

    response = await client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    latency = time.perf_counter() - start

    return ModelResponse(
        provider="OpenRouter",
        response=response.choices[0].message.content,
        latency=latency,
        success=True,
    )
