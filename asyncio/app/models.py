from dataclasses import dataclass


@dataclass
class ModelResponse:
    provider: str
    response: str
    latency: float
    success: bool