import os
from datetime import datetime
from dotenv import load_dotenv
import gradio as gr
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

load_dotenv()


def get_date():
    """Get the current date"""
    print("I was called")
    return datetime.now().strftime("%Y-%m-%d")


llm = ChatOllama(model="qwen2.5:3b")

system_prompt = """
You are a helpful assistant.
Answer all user's queries.
Use the get_date tool if the user is asking about the today's date.
"""

agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)


def chat(message, history):
    response = agent.invoke({"messages": [{"role": "user", "content": message}]})
    last_response = response["messages"][-1].content
    return last_response


with gr.Blocks() as demo:
    gr.Markdown("# AI Chatbot")
    gr.ChatInterface(fn=chat)

demo.launch()