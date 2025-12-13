from langchain.tools import tool
import os
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

@tool
def call_sleep_tool(number: str) -> str:
    """Call the given phone number and play a sleep message using Twilio."""
    from trying_twilio import call_sleep
    call_sleep(number)
    return f"Called {number} with sleep message."

@tool
def call_wake_tool(number: str) -> str:
    """Call the given phone number and play a wake message using Twilio."""
    from trying_twilio import call_wake
    call_wake(number)
    return f"Called {number} with wake message."

system_prompt = """You are an AI agent that can make phone calls to play sleep or wake messages using Twilio, Ask user if you are unsure if u have to make a sleep call or a waking call, You must only ever call one tool per user request"""
from langchain.tools import tool
prompt = PromptTemplate(
    input_variables=["input"],
    template=system_prompt + "\nUser: {input}\nAI:"
)

llm = OpenAI(temperature=0.6)
tools = [call_sleep_tool, call_wake_tool]
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")