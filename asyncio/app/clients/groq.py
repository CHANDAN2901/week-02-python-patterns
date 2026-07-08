from openai import AsyncOpenAI
import time

from app.config import GROQ_API_KEY
from app.models import ModelResponse

client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


async def ask_groq(prompt: str):

    start = time.perf_counter()

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    latency = time.perf_counter() - start

    return ModelResponse(
        provider="Groq",
        response=response.choices[0].message.content,
        latency=latency,
        success=True,
    )
