import asyncio
import time

from app.clients.openai import ask_openai
from app.clients.openrouter import ask_openrouter
from app.clients.groq import ask_groq


async def benchmark(prompt: str):

    start = time.perf_counter()

    results = await asyncio.gather(
        ask_openai(prompt),
        ask_openrouter(prompt),
        ask_groq(prompt),
        return_exceptions=True,
    )

    total = time.perf_counter() - start

    return results, total