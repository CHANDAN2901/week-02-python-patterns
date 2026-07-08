# Async LLM Benchmark

This project demonstrates how to use Python `asyncio` to call multiple LLM providers in parallel and compare their response times.

The script sends the same prompt to OpenAI, Groq, and OpenRouter at the same time, then prints a simple benchmark table with each provider's latency and the total wall-clock time.

## What This Project Teaches

This exercise is designed to show a few important Python concepts:

### 1. Asynchronous programming

The core idea is that network calls do not need to run one after another. Instead of waiting for one provider to finish before starting the next, the app starts all requests concurrently.

### 2. `async` / `await`

Each provider client exposes an asynchronous function. The `await` keyword lets Python pause a task while the request is in flight without blocking the whole program.

### 3. Concurrent execution with `asyncio.gather`

The `benchmark()` function runs all provider calls together using `asyncio.gather()`. That is the main reason the total time is closer to the slowest request than the sum of all requests.

### 4. Measuring latency

Each client measures its own response time with `time.perf_counter()`. The benchmark also measures total elapsed time so you can compare per-provider latency against the full concurrent run.

### 5. Environment-based configuration

API keys are loaded from environment variables using `python-dotenv`. This keeps secrets out of the codebase and makes local setup easier.

### 6. Simple result modeling

The `ModelResponse` dataclass stores the provider name, returned text, latency, and success flag in a structured way.

### 7. Clean terminal output

The final results are displayed with `rich`, which makes the benchmark easier to read in the terminal.

## Project Flow

1. `main.py` defines the prompt and starts the benchmark.
2. `app/benchmark.py` launches all provider requests concurrently.
3. Each client in `app/clients/` sends the same prompt to a different API.
4. The result is wrapped in a `ModelResponse` object.
5. `main.py` prints a table with latency results and total time.

## Project Structure

```text
main.py
app/
	benchmark.py      # Runs all provider calls concurrently
	config.py         # Loads environment variables
	logger.py         # Shared console instance
	models.py         # Dataclass for response data
	clients/
		openai.py       # OpenAI client wrapper
		groq.py         # Groq client wrapper
		openrouter.py    # OpenRouter client wrapper
```

## Requirements

- Python 3.12+
- API keys for the providers you want to use

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Copy `.env.example` to `.env`.
4. Add your API keys.

Example:

```bash
cp .env.example .env
```

Then fill in:

```env
OPENAI_API_KEY=
GROQ_API_KEY=
OPENROUTER_API_KEY=
```

## Run The Project

```bash
python main.py
```

The script will send one prompt to all three providers and print a benchmark table in the terminal.

## How It Works In Detail

The important part of the project is this pattern:

```python
results = await asyncio.gather(
		ask_openai(prompt),
		ask_openrouter(prompt),
		ask_groq(prompt),
		return_exceptions=True,
)
```

Because the requests are launched together, the event loop can handle them concurrently. This is especially useful for API calls, where the program spends most of its time waiting on network I/O rather than doing CPU work.

Each provider client follows the same basic pattern:

1. Record the start time.
2. Send a chat completion request.
3. Measure elapsed time.
4. Return a `ModelResponse` object.

That shared shape makes it easy to compare providers without writing separate output code for each one.

## Why This Is Useful

This project is a compact example of a real-world asyncio use case:

- fan out the same request to multiple services
- compare response times
- keep the UI simple while the network work happens concurrently
- isolate each provider behind a small wrapper function

## Extending The Exercise

You can build on this project by:

- adding more providers
- storing responses to a file or database
- running multiple prompts and averaging the latency
- comparing token usage as well as speed
- adding retries or timeout handling

## Troubleshooting

- If a provider fails, check that the corresponding API key is set in `.env`.
- If the script cannot import packages, confirm the virtual environment is active.
- If you want to skip a provider, remove or comment out its call in `app/benchmark.py`.

## License

No license has been added yet.
