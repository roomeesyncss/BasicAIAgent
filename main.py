
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.file import FileTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="gemma2-9b-it"),
    tools=[FileTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

agent.print_response(
    "What is the most advanced LLM currently? Save the answer to a file named 'advanced_llm.txt'."
)
