from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma:2b")

@tool
def get_weather(city: str) -> str:
    """Devuelve el clima para la ciudad dada."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)