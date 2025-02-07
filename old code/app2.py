import gradio as gr
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI


# Replace YOUR_API_KEY_HERE with your actual API key
llm = ChatOpenAI(temperature=0.9, model_name="gpt-4o")

from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()


# Ignore deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Your example data setup
examples = [
    {"query": "What is a cellphone?", "answer": "A cellphone is a magical device..."},
    # (Your other examples here)
]

example_template = "Question: {query}\nResponse: {answer}"

example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)

prefix = "You are a 5-year-old girl, who is very funny and sweet..."
suffix = "Question: {userInput}\nResponse:"

example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=200
)

new_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["userInput"],
    example_separator="\n"
)

def generate_response(userInput, task_type, age_group, word_limit):
    formatted_prompt = new_prompt_template.format(userInput=userInput)
    response = llm.invoke([HumanMessage(content=formatted_prompt)])
    return response.content

# Gradio UI setup
with gr.Blocks() as demo:
    gr.Markdown("# Marketing Tool")
    
    user_input = gr.Textbox(placeholder="Enter text...", label="Input Text", lines=5)
    task_type = gr.Dropdown(choices=["Write a sales copy", "Create a tweet", "Write a product description"], label="Task")
    age_group = gr.Dropdown(choices=["Kid", "Adult", "Senior Citizen"], label="Age Group")
    word_limit = gr.Slider(minimum=1, maximum=200, value=25, label="Word Limit")
    submit_btn = gr.Button("Generate")
    
    output_text = gr.Textbox(label="Output", lines=5)
    
    submit_btn.click(fn=generate_response, inputs=[user_input, task_type, age_group, word_limit], outputs=output_text)

demo.launch()

import os
print("API Key Loaded:", os.getenv("OPENAI_API_KEY"))
