# AI Calling Assistant

An AI-powered calling assistant that automates wake-up and sleep reminder calls using Twilio, LangChain, and OpenAI GPT. The system supports time-based scheduling, chat-triggered calls, and customizable voice messages with optional audio playback.

## What it Does

- Places automated reminder calls at scheduled times
- Speaks AI-generated messages and optionally plays audio after the message
- Allows GPT tools to trigger calls via chat commands or webhooks
- Supports scheduling through n8n with time-based checks

## How to Run

- **streamlit_main.py**  
  Run a Streamlit interface to chat with and test the assistant (GPT-like UI)

- **main.py**  
  Run the assistant directly using Python for local testing and debugging

- **server.py**  
  Run a FastAPI server that serves Twilio XML (TwiML) responses during calls

- **ai-calling-n8n**  
  Contains the n8n workflow logic used to schedule and trigger calls automatically

## Tech Stack

Python, FastAPI, Streamlit, LangChain, OpenAI GPT, Twilio, n8n

## Notes

- Solo project focused on backend automation and AI orchestration
- Frontend kept minimal and used only for testing
