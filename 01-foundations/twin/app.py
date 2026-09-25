from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):

    # Convert Gradio history format to OpenAI message format
    # Gradio history is a list of [user_message, assistant_response] pairs
    messages = system + [{"role": "system", "content": message}]
    
    for h in history:
        if isinstance(h, (list, tuple)) and len(h) == 2:
            # Gradio format: [user_message, assistant_response]
            messages.append({"role": "user", "content": h[0]})
            messages.append({"role": "assistant", "content": h[1]})
        elif isinstance(h, dict):
            # Already in dict format
            messages.append(h)
    
    # Add current user message
    messages.append({"role": "user", "content": message})
    
    response = openai.chat.completions.create(model="gpt-5.4-mini", messages=messages, tools=tools)
 
    while response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model="gpt-5.4-mini", messages=messages, tools=tools)
    return response.choices[0].message.content

'''
if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
'''

if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    ).launch()