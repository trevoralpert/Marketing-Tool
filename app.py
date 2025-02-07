import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain_community.chat_models import ChatOpenAI

from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def getLLMResponse(query,age_option,tasktype_option):
    llm = ChatOpenAI(temperature=.9,model_name="gpt-4")
    if age_option == "Kid":
        examples = [
            {
                "query": "What is a cellphone?",
                "answer": "A cellphone is a magical device for playing games and taking pictures and videos, but be careful it turns grown-ups into zombies."
            }, {
                "query": "What are your dreams?",
                "answer": "My dreams are like a colorful adventure where everyone has a pony and I ride a dragon named Sparkles."
            }, {
                "query": "What are your ambitions?",
                "answer": "I want to be a super funny comedian who makes fun of grown-ups by turning them into clowns."
            }, {
                "query": "What happens when you get sick?",
                "answer": "When I get sick it's like a sneaky elf put a spell on me to make me sneeze all over all the grown-ups."
            }, {
                "query": "How much do you love your dad?",
                "answer": "I love my dad to the moon and back, except when he watches the grown-up news when my cartoons are on."
            }
        ]
    elif age_option=="Adult":
        examples = [
            {
                "query": "What is a cellphone?",
                "answer": "A cellphone is a powerful tool for communication, work, and staying connected with loved ones. It can also be a big distraction if you're not careful!"
            }, {
                "query": "What are your dreams?",
                "answer": "My dreams are about finding happiness, balance, and success—whether in my career, relationships, or personal growth."
            }, {
                "query": "What are your ambitions?",
                "answer": "I want to excel in my career, make a positive impact in my community, and achieve financial stability while still making time for what matters."
            }, {
                "query": "What happens when you get sick?",
                "answer": "When I get sick, I try to rest, drink plenty of fluids, and take care of my responsibilities as best I can. But honestly, being sick just reminds me how much I need a break."
            }, {
                "query": "How much do you love your dad?",
                "answer": "I love my dad deeply. As I’ve grown older, I’ve realized how much he sacrificed and how much wisdom he has to offer."
            }
        ]
    elif age_option=="Senior Citizen":
        examples = [
            {
                "query": "What is a cellphone?",
                "answer": "A cellphone is a little computer in your pocket. I remember when phones had cords and stayed in one place! Now, I can talk to my grandchildren and even see their faces with just a tap."
            }, {
                "query": "What are your dreams?",
                "answer": "At this stage, my dreams are about good health, spending time with family, and leaving behind a legacy of love and wisdom."
            }, {
                "query": "What are your ambitions?",
                "answer": "At this point in life, my ambition is to enjoy every moment, pass down knowledge to younger generations, and maybe finally finish that book I've been meaning to write."
            }, {
                "query": "What happens when you get sick?",
                "answer": "When I get sick, I take it seriously. I’ve learned that health is precious, and a small cold can feel like a big battle. Rest, good food, and a bit of patience go a long way."
            }, {
                "query": "How much do you love your dad?",
                "answer": "I love my dad more than words can express. I miss him every day, and I cherish the lessons he taught me. If I could, I’d give him one more hug."
            }
        ]
    else:
        examples = [
            {
                "query": "What is a cellphone?",
                "answer": "A cellphone is a device used for communication, entertainment, and work."
            }
        ]

    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables=["query","answer"],
        template=example_template
    )

    prefix = """You are a {template_ageoption}, who is asked to {template_tasktype_option}.
    Here are some examples:
    """

    suffix = """
    Question: {userInput}
    Response: """

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
        input_variables=["userinput","template_ageoption","template_tasktype_option"],
        example_separator="\n"
    )

    query = form_input
    p = new_prompt_template.format(userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option)
    print(p)

    answer = llm.invoke([HumanMessage(content=p)])

    print(answer.content)
    return answer.content

#UI starts here

st.set_page_config(page_title="Marketing Tool",
                   page_icon='✅',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Hey, How can I help you?")

form_input = st.text_area('Enter text', height=275)

tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('Write a sales copy', 'Create a tweet', 'Write a product description'),key=1)

age_option= st.selectbox(
    'For which age group?',
    ('Kid', 'Adult', 'Senior Citizen'),key=2)

numberOfWords= st.slider('Words limit', 1, 200, 25)

submit = st.button("Generate")

if submit:
    st.write(getLLMResponse(form_input,tasktype_option,age_option))

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
