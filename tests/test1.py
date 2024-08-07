from classes import AnthropicDriver, OpenAiDriver
from hypster import Options, lazy

OpenAiDriver = lazy(OpenAiDriver)
AnthropicDriver = lazy(AnthropicDriver)

llm_driver = Options({
    "anthropic": AnthropicDriver(max_tokens=1000),
    "openai": OpenAiDriver(max_tokens=500)
}, default="anthropic")