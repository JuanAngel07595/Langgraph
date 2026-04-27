from langchain.agents import create_agent
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma:2b")



def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

