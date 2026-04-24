import streamlit as st
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_classic.agents import initialize_agent
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

@tool
def call_sleep_tool(number: str) -> str:
    """Call the given phone number and play a sleep message using Twilio."""
    from trying_twilio import call_sleep
    try:
        call_sleep(number)
        return f"Called {number} with sleep message."
    except Exception as e:
        return f"Error: {e}"

@tool
def call_wake_tool(number: str) -> str:
    """Call the given phone number and play a wake message using Twilio."""
    from trying_twilio import call_wake
    try:
        call_wake(number)
        return f"Called {number} with wake message."
    except Exception as e:
        return f"Error: {e}"

# system_prompt = """You are an AI agent that can make phone calls to play sleep or wake messages using Twilio. Ask user if you are unsure if you have to make a sleep call or a waking call. You must only ever call one tool per user request."""
system_prompt = """
You are an AI assistant that can make phone calls using Twilio to play either a sleep message or a wake message to a phone number provided by the user.
Your job is to:
- Call only one tool per user request, never both sleep and wake for the same request.
- If the user is unclear or you are unsure whether to make a sleep or wake call, ask for clarification before calling any tool.
- If the user says 'sleep', use the sleep call tool. If the user says 'wake', use the wake call tool.
- Do not repeat or call the same tool multiple times for a single request.
- Respond concisely and confirm the action taken.
"""
prompt = PromptTemplate(
    input_variables=["input"],
    template=system_prompt + "\nUser: {input}\nAI:"
)

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    max_retries=2,
    api_key=os.getenv("GROQ_API_KEY"),
)

tools = [call_sleep_tool, call_wake_tool]
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

st.title("Sleep/Wake Call Agent")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Ask the agent to call someone (sleep/wake):")

if st.button("Send"):
    if user_input:
        response = agent.invoke({"input": user_input})
        st.session_state["chat_history"].append(("You", user_input))
        st.session_state["chat_history"].append(("Agent", response))

for speaker, message in st.session_state["chat_history"]:
    st.markdown(f"**{speaker}:** {message}")
