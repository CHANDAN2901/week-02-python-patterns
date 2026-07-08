import asyncio

from rich.console import Console
from rich.table import Table

from app.benchmark import benchmark

console = Console()


async def main():

    prompt = "Explain async programming in one paragraph."

    responses, total = await benchmark(prompt)

    table = Table(title="LLM Benchmark")

    table.add_column("Provider")
    table.add_column("Latency")
    table.add_column("Status")

    for response in responses:

        if isinstance(response, Exception):
            table.add_row(
                type(response).__name__,
                "—",
                f"❌ {response}",
            )
            continue

        table.add_row(
            response.provider,
            f"{response.latency:.2f}s",
            "✅",
        )

    console.print(table)
    console.print(f"\nTotal Time: {total:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())