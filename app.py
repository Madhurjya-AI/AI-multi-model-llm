import gradio as gr
from models import load_models, get_model
from router import classify_task

load_models()

def chat_agent(message, history):
    task = classify_task(message)
    model = get_model(task)
    prompt = message
    result = model(prompt)[0]["generated_text"]
    return result

iface = gr.ChatInterface(
    fn=chat_agent,
    title="Multi-Model AI Coding Assistant",
    description="Ask code questions, general questions. System chooses best model.",
    examples=[
        ["Write a Python function to reverse a string."],
        ["What is the theory of relativity?"]
    ]
)

iface.launch()